import sys
import os

# Tambahkan direktori induk ke path agar dapat melakukan import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)

