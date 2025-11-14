# Manajemen User

## Daftar User Saat Ini

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Administrator |
| driver1 | pass1 | Pengemudi |
| driver2 | pass2 | Pengemudi |
| driver3 | pass3 | Pengemudi |

## Cara Menambah User Baru

### Metode 1: Edit Manual di app.py

1. Buka file `app.py`
2. Cari bagian ini (sekitar baris 14-20):

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    "driver2": "pass2",
    "driver3": "pass3"
}
```

3. Tambahkan user baru:

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    "driver2": "pass2",
    "driver3": "pass3",
    "budi_santoso": "budi2024",      # User baru 1
    "ahmad_wijaya": "ahmad123",      # User baru 2
    "siti_nurhaliza": "siti456"      # User baru 3
}
```

4. Save file
5. Refresh aplikasi di browser (atau restart streamlit)

### Metode 2: Best Practice untuk Production

Untuk aplikasi production, sebaiknya user disimpan di database atau file terpisah.

**Contoh dengan file JSON:**

1. Buat file `users.json`:
```json
{
  "admin": {"password": "admin123", "role": "admin"},
  "driver1": {"password": "pass1", "role": "driver"},
  "budi": {"password": "budi123", "role": "driver"}
}
```

2. Update `app.py` untuk load dari file

## Keamanan Password

⚠️ **Untuk Production:**

Saat ini password disimpan plain text (tidak aman). Untuk production:

1. **Gunakan hashing:**
```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Simpan hash, bukan password asli
USERS = {
    "admin": hash_password("admin123"),
    # dst...
}
```

2. **Gunakan database:**
   - SQLite untuk aplikasi kecil
   - PostgreSQL/MySQL untuk skala besar
   - Firebase Authentication
   - Supabase

3. **Implementasi:**
   - Password reset via email
   - 2FA (Two-Factor Authentication)
   - Session timeout
   - Password strength requirements

## Tips Manajemen User

### 1. Konvensi Penamaan Username
- Gunakan nama depan + underscore/angka
- Contoh: `budi_s`, `ahmad1`, `driver_01`
- Hindari spasi
- Huruf kecil semua

### 2. Password Policy
- Minimal 8 karakter
- Kombinasi huruf + angka
- Ganti password berkala (3-6 bulan)
- Jangan gunakan password yang sama

### 3. Role Management
Untuk implementasi role (admin vs driver):

```python
USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "can_delete": True,
        "can_edit_users": True
    },
    "driver1": {
        "password": "pass1",
        "role": "driver",
        "can_delete": False,
        "can_edit_users": False
    }
}
```

## Menghapus User

Edit `app.py` dan hapus baris user yang tidak diperlukan:

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    # "driver2": "pass2",  # User ini dihapus (dikomentar)
    "driver3": "pass3"
}
```

## Reset Password User

Ganti password di dictionary:

```python
USERS = {
    "admin": "admin123",
    "driver1": "password_baru",  # Password diganti
    "driver2": "pass2"
}
```

## Implementasi Database (Opsional)

Untuk sistem yang lebih robust, gunakan database:

### Dengan SQLite (built-in Python):

```python
import sqlite3
import hashlib

# Create users table
conn = sqlite3.connect('checklist.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password_hash TEXT,
        role TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# Add user
def add_user(username, password, role='driver'):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    c.execute('INSERT INTO users VALUES (?, ?, ?, ?)',
              (username, password_hash, role, None))
    conn.commit()

# Verify login
def verify_login(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    c.execute('SELECT * FROM users WHERE username=? AND password_hash=?',
              (username, password_hash))
    return c.fetchone() is not None
```

## Backup & Restore

Sebelum edit user, backup dulu:

```bash
# Backup
cp app.py app.py.backup

# Restore jika ada masalah
cp app.py.backup app.py
```

## Monitoring Login

Untuk track siapa yang login kapan, tambahkan logging:

```python
import logging
from datetime import datetime

logging.basicConfig(filename='login.log', level=logging.INFO)

# Di fungsi login:
if username in USERS and USERS[username] == password:
    logging.info(f"{datetime.now()} - Login success: {username}")
    # ...
else:
    logging.warning(f"{datetime.now()} - Login failed: {username}")
```

## FAQ

**Q: Berapa maksimal user yang bisa ditambahkan?**
A: Tidak ada limit, tapi untuk >50 user sebaiknya gunakan database.

**Q: Bisakah user ganti password sendiri?**
A: Saat ini belum ada fitur ini. Perlu develop fitur "Change Password".

**Q: Bagaimana jika lupa password?**
A: Saat ini harus kontak admin untuk reset manual. Bisa develop fitur "Forgot Password" dengan email.

**Q: Bisakah satu orang punya multiple account?**
A: Bisa, tapi tidak disarankan untuk keperluan audit trail.

## Kontak

Untuk bantuan manajemen user:
- Hubungi Admin IT
- Email: [admin email]
