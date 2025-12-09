class User:
    """User model representing a user in the database"""
    
    def __init__(self, id=None, username=None, password=None, email=None, nama=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.nama = nama
    
    def to_dict(self):
        """Convert user to dictionary (excluding password)"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'nama': self.nama
        }

    @classmethod
    def from_dict(cls, data):
        """Create User instance from dictionary"""
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            nama=data.get('nama')
        )

