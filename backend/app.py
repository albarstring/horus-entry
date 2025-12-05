from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="horus_albar_db"
    )

#register
@app.post("/users/register")
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    nama = data.get("nama")

    if not username or not password:
        return jsonify({"message": "Username dan password wajib diisi"}), 400

    hashed = generate_password_hash(password)

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, password, email, nama)
            VALUES (%s,%s,%s,%s)
        """,(username, hashed, email, nama))

        conn.commit()
        return jsonify({"message":"Registrasi Berhasil"}), 201

    except mysql.connector.errors.IntegrityError:
        return jsonify({"message":"Username sudah digunakan"}),400

    finally:
        cursor.close()
        conn.close()


#login 
@app.post("/users/login")
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and check_password_hash(user["password"], password):
        return jsonify({
            "message": "Login berhasil",
            "token": "fake-token"
        }),200

    return jsonify({"message": "Username atau password salah"}), 401


#mengambil semua useer
@app.get("/users")
def get_users():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, username, email, nama FROM users")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result), 200

#mengupdate user
@app.put("/users/<int:user_id>")
def update_user(user_id):
    data = request.json
    username = data.get("username")
    email = data.get("email")
    nama = data.get("nama")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users SET username=%s, email=%s, nama=%s WHERE id=%s
    """, (username, email, nama, user_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Data user berhasil diperbarui"}), 200

#menghapus user
@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "User berhasil dihapus"}), 200


#menjalankan server
if __name__ == "__main__":
    app.run(debug=True)