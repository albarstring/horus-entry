from flask_cors import CORS
from app.config import Config

# Initialize CORS with explicit origins/methods/headers so all routes return
# the correct Access-Control-* headers (especially for DELETE requests).
def init_cors(app):
    CORS(app, resources={
        r"/*": {
            "origins": Config.CORS_ORIGINS if hasattr(Config, "CORS_ORIGINS") else "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
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

