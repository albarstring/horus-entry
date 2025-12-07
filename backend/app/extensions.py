from flask_cors import CORS
from app.config import Config

# Initialize extensions with CORS configuration
cors = CORS(resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Database connection helper
class Database:
    def __init__(self, config):
        self.config = config
    
    def get_connection(self):
        import mysql.connector
        return mysql.connector.connect(
            host=self.config.DB_HOST,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD,
            database=self.config.DB_NAME
        )
    
    def init_app(self, app):
        pass

db = Database(Config)

