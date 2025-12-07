# Migrations

Folder ini untuk menyimpan database migrations jika menggunakan Flask-Migrate.

Untuk setup Flask-Migrate (opsional):
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**Catatan:** Project ini saat ini menggunakan MySQL langsung tanpa Flask-Migrate. 
Jika ingin menggunakan Flask-Migrate di masa depan, install terlebih dahulu:
```bash
pip install flask-migrate
```

