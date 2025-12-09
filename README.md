# Horus Exam Project

Project ini adalah aplikasi full-stack untuk manajemen pengguna dengan backend Flask dan frontend Vue.js.

## Struktur Project

```
horus/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── extensions.py          # db, cors
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── user_service.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── validators.py
│   ├── .env.example
│   ├── requirements.txt
│   └── run.py                     # entry point: `python run.py`
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── UserTable.vue
│   │   │   └── SearchBar.vue
│   │   ├── views/
│   │   │   ├── Login.vue
│   │   │   ├── Register.vue
│   │   │   ├── Dashboard.vue
│   │   │   └── UpdateUser.vue
│   │   ├── router/
│   │   │   └── index.js
│   │   ├── store/
│   │   │   └── auth.js
│   │   ├── services/
│   │   │   └── api.js             # axios instance
│   │   ├── App.vue
│   │   └── main.js
│   ├── public/
│   │   └── index.html
│   ├── .env.example
│   └── package.json
│
└── README.md
```

## Setup Backend

1. Masuk ke folder backend:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Buat file `.env` dari `.env.example`:
```bash
cp .env.example .env
```

4. Edit file `.env` dan sesuaikan konfigurasi database:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=horus_albar_db
```

5. Jalankan aplikasi:
```bash
python run.py
```

Backend akan berjalan di `http://127.0.0.1:5000`

## Setup Frontend

1. Masuk ke folder frontend:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Buat file `.env` dari `.env.example`:
```bash
cp .env.example .env
```

4. Edit file `.env` jika perlu (default sudah benar):
```
VITE_API_BASE_URL=http://127.0.0.1:5000
```

5. Jalankan development server:
```bash
npm run dev
```

Frontend akan berjalan di `http://localhost:5173` (atau port lain yang tersedia)

## Fitur

- ✅ Login & Register
- ✅ Dashboard dengan tabel pengguna
- ✅ Search/Filter pengguna
- ✅ Update pengguna
- ✅ Delete pengguna
- ✅ Vue Router untuk navigasi
- ✅ State management dengan composables
- ✅ API service layer
- ✅ Desain hitam putih dengan Tailwind CSS

## Teknologi

**Backend:**
- Flask
- MySQL
- Flask-CORS
- Python-dotenv

**Frontend:**
- Vue.js 3
- Vue Router
- Tailwind CSS
- Vite

