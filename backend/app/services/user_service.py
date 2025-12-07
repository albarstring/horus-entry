from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from app.config import Config
from app.models.user import User


class UserService:
    @staticmethod
    def get_db_connection():
        """Get database connection"""
        return mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
    
    @staticmethod
    def register(username, password, email, nama):
        """Register a new user"""
        hashed = generate_password_hash(password)
        conn = UserService.get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO users (username, password, email, nama)
                VALUES (%s, %s, %s, %s)
            """, (username, hashed, email, nama))
            
            conn.commit()
            return {"message": "Registrasi Berhasil"}, 201
            
        except mysql.connector.errors.IntegrityError:
            return {"message": "Username sudah digunakan"}, 400
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def login(username, password):
        """Login user"""
        conn = UserService.get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if user_data and check_password_hash(user_data["password"], password):
            return {
                "message": "Login berhasil",
                "token": "fake-token"
            }, 200
        
        return {"message": "Username atau password salah"}, 401
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        conn = UserService.get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT id, username, email, nama FROM users")
        result = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return result, 200
    
    @staticmethod
    def update_user(user_id, username, email, nama):
        """Update user data"""
        conn = UserService.get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Update data
        cursor.execute("""
            UPDATE users SET username=%s, email=%s, nama=%s WHERE id=%s
        """, (username, email, nama, user_id))
        
        # Check if user exists
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return {"message": "User tidak ditemukan"}, 404
        
        conn.commit()
        
        # Get updated user
        cursor.execute("SELECT id, username, email, nama FROM users WHERE id=%s", (user_id,))
        updated_user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return {
            "message": "Data user berhasil diperbarui",
            "user": updated_user
        }, 200
    
    @staticmethod
    def delete_user(user_id):
        """Delete user"""
        conn = UserService.get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return {"message": "User berhasil dihapus"}, 200

