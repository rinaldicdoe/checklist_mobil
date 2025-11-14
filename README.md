# Form Checklist Pemeriksaan Mobil - Riyadh Group

Aplikasi web untuk melakukan pemeriksaan kelayakan kendaraan secara sistematis dengan fitur lengkap:
- 🔐 Sistem login untuk multiple pengemudi
- 📷 Upload foto kondisi mobil
- 📝 Field catatan/komentar
- 📊 Auto-send ke Google Sheets

## Instalasi

1. Clone atau download repository ini

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Opsional) Setup Google Sheets API:
   - Lihat panduan lengkap di file `SETUP_GOOGLE_SHEETS.md`
   - Download credentials JSON dari Google Cloud Console
   - Simpan sebagai `credentials.json` di folder aplikasi

## Menjalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## Login Default

- **Username:** `admin` / **Password:** `admin123`
- **Username:** `driver1` / **Password:** `pass1`
- **Username:** `driver2` / **Password:** `pass2`
- **Username:** `driver3` / **Password:** `pass3`

## Fitur Utama

### 🔐 Sistem Login Multi-User
- Setiap pengemudi punya akun sendiri
- Data tercatat dengan username pengemudi
- Logout untuk ganti user

### 📋 Checklist Lengkap
- **Sebelum pemeriksaan:** STNK, SIM, safety cone
- **Kondisi eksterior:** Body, kaca, lampu, ban, dll
- **Kondisi interior:** Kabin, AC, sabuk pengaman, dll
- **Kelengkapan:** APAR, P3K, dongkrak, segitiga
- **Kelistrikan & Engine:** Aki, oli, radiator, dll
- **Test drive:** Akselerasi, pengereman, transmisi

### 📷 Upload Foto
- Upload multiple foto sekaligus
- Format: JPG, JPEG, PNG
- Preview langsung di aplikasi
- Info foto tersimpan untuk dokumentasi

### 📝 Catatan/Komentar
- Text area untuk catatan detail
- Dokumentasi kondisi khusus
- Mencatat kerusakan atau kebutuhan perbaikan

### 📊 Google Sheets Integration
- Data otomatis tersimpan ke Google Sheets
- Real-time sync
- Mudah untuk reporting dan analisis
- Akses dari mana saja

## Struktur File

```
checklist_mobil/
├── app.py                      # Aplikasi utama
├── requirements.txt            # Dependencies Python
├── credentials.json            # (Optional) Google Sheets credentials
├── README.md                   # Dokumentasi ini
├── SETUP_GOOGLE_SHEETS.md     # Panduan setup Google Sheets
├── PANDUAN_PENGGUNA.md        # Panduan untuk user
└── .gitignore                 # File yang diabaikan git
```

## Menambah User Baru

Edit file `app.py` di bagian dictionary `USERS`:

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    "username_baru": "password_baru"  # Tambahkan di sini
}
```

## Dokumentasi Lengkap

- **Setup Google Sheets:** Baca `SETUP_GOOGLE_SHEETS.md`
- **Panduan Pengguna:** Baca `PANDUAN_PENGGUNA.md`

## Troubleshooting

### Aplikasi tidak bisa dijalankan
```bash
# Install ulang dependencies
pip install -r requirements.txt --upgrade
```

### Data tidak masuk ke Google Sheets
- Cek file `credentials.json` sudah ada
- Pastikan Google Sheets API sudah di-enable
- Cek Google Sheet sudah di-share ke service account
- Lihat console untuk error message

### Error import module
```bash
# Pastikan semua package terinstall
pip install streamlit gspread google-auth Pillow
```

## Keamanan

⚠️ **PENTING:**
- Jangan commit file `credentials.json` ke Git
- Gunakan `.gitignore` untuk exclude credentials
- Ganti password default untuk production
- Simpan credentials di tempat aman

## Pengembangan Selanjutnya

- ✅ Login system
- ✅ Upload foto
- ✅ Field catatan
- ✅ Google Sheets integration
- ⏳ Export ke PDF
- ⏳ Dashboard analytics
- ⏳ Email notification
- ⏳ Database historis

## Support

Untuk bantuan lebih lanjut, hubungi:
- Admin IT Riyadh Group
- Buat issue di repository ini

## Lisensi

© 2025 Riyadh Group. All rights reserved.
