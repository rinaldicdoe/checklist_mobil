# 🚀 Quick Start Guide

## Langkah Cepat Memulai

### 1. Install Dependencies (5 menit)
```bash
cd checklist_mobil
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi (1 menit)
```bash
streamlit run app.py
```

Aplikasi otomatis terbuka di browser: `http://localhost:8501`

### 3. Login (30 detik)
- Username: `admin`
- Password: `admin123`
- Klik "Login"

### 4. Isi Checklist (5-10 menit)
1. Form identitas otomatis terisi
2. Isi nomor kendaraan
3. Checklist semua item (Ya/Tidak)
4. Upload foto kondisi mobil (opsional)
5. Tambah catatan jika ada
6. Klik "✅ Submit Checklist"

### 5. Lihat Hasil
- Ringkasan data ditampilkan
- Hasil checklist dengan icon ✅/❌
- Data tersimpan (jika Google Sheets sudah disetup)

---

## Setup Google Sheets (Opsional - 15 menit)

Jika ingin data otomatis masuk ke Google Sheets:

### Langkah Singkat:
1. **Google Cloud Console**
   - Buat project baru
   - Enable Google Sheets API
   - Buat Service Account
   - Download JSON credentials

2. **Setup File**
   - Rename file jadi `credentials.json`
   - Copy ke folder `checklist_mobil`

3. **Google Sheets**
   - Buat sheet baru: "Checklist Mobil Riyadh"
   - Share ke email service account (dari credentials)
   - Beri permission Editor

4. **Test**
   - Submit checklist
   - Cek data masuk ke Google Sheets

📖 **Panduan lengkap:** Lihat file `SETUP_GOOGLE_SHEETS.md`

---

## Menambah Pengemudi Baru

Edit file `app.py`, cari:

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    # Tambah di bawah:
    "budi": "password123",
    "ahmad": "pass456"
}
```

Save file, refresh browser.

---

## Tips Singkat

✅ **DO:**
- Upload foto yang jelas
- Isi semua checklist items
- Tulis catatan detail jika ada masalah
- Logout setelah selesai

❌ **DON'T:**
- Skip item checklist
- Upload file bukan foto (PDF, DOC, dll)
- Share password ke orang lain
- Lupa logout di komputer bersama

---

## Troubleshooting Cepat

**Masalah:** `ModuleNotFoundError: No module named 'streamlit'`
```bash
pip install -r requirements.txt
```

**Masalah:** Port 8501 sudah digunakan
```bash
streamlit run app.py --server.port 8502
```

**Masalah:** Data tidak ke Google Sheets
- Cek file `credentials.json` ada atau tidak
- Aplikasi tetap jalan, cuma data tidak auto-save ke Sheets

---

## Fitur Utama yang Baru

| Fitur | Keterangan |
|-------|-----------|
| 🔐 Login | Beda pengemudi, beda akun |
| 📷 Upload Foto | Multiple foto sekaligus |
| 📝 Catatan | Text area untuk detail |
| 📊 Google Sheets | Auto-save ke cloud |

---

## Bantuan Lebih Lanjut

- **Panduan User:** `PANDUAN_PENGGUNA.md`
- **Setup Sheets:** `SETUP_GOOGLE_SHEETS.md`
- **README Lengkap:** `README.md`

---

**Selamat menggunakan! 🚗✅**
