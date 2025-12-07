def validate_register_data(data):
    """Validate registration data"""
    errors = []
    
    if not data.get('username'):
        errors.append('Username wajib diisi')
    if not data.get('password'):
        errors.append('Password wajib diisi')
    if not data.get('email'):
        errors.append('Email wajib diisi')
    if not data.get('nama'):
        errors.append('Nama wajib diisi')
    
    return errors


def validate_login_data(data):
    """Validate login data"""
    errors = []
    
    if not data.get('username'):
        errors.append('Username wajib diisi')
    if not data.get('password'):
        errors.append('Password wajib diisi')
    
    return errors


def validate_update_data(data):
    """Validate update data"""
    errors = []
    
    if not data.get('username'):
        errors.append('Username wajib diisi')
    if not data.get('email'):
        errors.append('Email wajib diisi')
    if not data.get('nama'):
        errors.append('Nama wajib diisi')
    
    return errors

