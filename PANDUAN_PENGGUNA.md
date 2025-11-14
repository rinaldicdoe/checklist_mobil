# Panduan Pengguna - Aplikasi Checklist Mobil

## Fitur-Fitur Baru

### 1. 🔐 Sistem Login
- Setiap pengemudi memiliki akun sendiri
- Username otomatis terisi di form
- Data tercatat dengan user yang login

**Akun Default:**
- Username: `admin` / Password: `admin123`
- Username: `driver1` / Password: `pass1`
- Username: `driver2` / Password: `pass2`
- Username: `driver3` / Password: `pass3`

### 2. 📷 Upload Foto Kondisi Mobil
- Upload multiple foto sekaligus
- Format: JPG, JPEG, PNG
- Preview foto langsung terlihat
- Info foto tersimpan di database

### 3. 📝 Field Catatan/Komentar
- Tambahkan catatan tambahan
- Contoh: kondisi khusus, kerusakan detail, dll
- Text area yang luas untuk deskripsi lengkap

### 4. 📊 Auto-Send ke Google Sheets
- Data otomatis tersimpan ke Google Sheets
- Real-time sync
- Bisa diakses dari mana saja
- Mudah untuk analisis dan reporting

## Cara Menggunakan

### A. Login
1. Buka aplikasi
2. Masukkan username dan password
3. Klik tombol "Login"
4. Jika berhasil, akan masuk ke form checklist

### B. Mengisi Form Checklist
1. **Identitas** akan terisi otomatis (nama = username)
2. Isi **Nomor Kendaraan**
3. Pilih **Tanggal dan Waktu** (default hari ini)
4. Checklist semua item dengan memilih **Ya** atau **Tidak**

### C. Upload Foto
1. Scroll ke bagian "Upload Foto Kondisi Mobil"
2. Klik "Browse files"
3. Pilih satu atau lebih foto
4. Foto akan terpreview otomatis

### D. Tambahkan Catatan
1. Di bagian "Catatan/Komentar"
2. Ketik catatan tambahan jika ada
3. Contoh: "Ban kiri depan tekanannya kurang, perlu dipompa"

### E. Submit
1. Klik tombol **"✅ Submit Checklist"**
2. Sistem akan:
   - Validasi data
   - Mengirim ke Google Sheets (jika sudah setup)
   - Menampilkan ringkasan data
3. Lihat hasil checklist dengan icon ✅ (Ya) atau ❌ (Tidak)

### F. Logout
1. Klik tombol **"🚪 Logout"** di pojok kanan atas
2. Kembali ke halaman login

## Menambah User Baru

Edit file `app.py` di bagian:

```python
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    "driver2": "pass2",
    "driver3": "pass3",
    "namauser_baru": "password_baru"  # Tambahkan di sini
}
```

## Tips Penggunaan

1. **Foto:**
   - Upload foto yang jelas dan terang
   - Ambil foto dari berbagai sudut
   - Fokuskan pada area yang bermasalah

2. **Catatan:**
   - Tulis detail masalah yang ditemukan
   - Cantumkan lokasi kerusakan/kondisi
   - Sertakan tingkat urgensi jika perlu

3. **Checklist:**
   - Jangan skip item apapun
   - Jika ada keraguan, pilih "Tidak" dan beri catatan
   - Pastikan test drive dilakukan dengan aman

## Akses Data di Google Sheets

Setelah submit, data bisa dilihat di Google Sheets:
1. Buka spreadsheet "Checklist Mobil Riyadh"
2. Setiap row = satu submission
3. Data tersusun rapih dalam kolom-kolom
4. Bisa difilter, sort, dan analisa

## Troubleshooting

**Data tidak masuk ke Google Sheets:**
- Cek koneksi internet
- Pastikan file `credentials.json` sudah ada
- Lihat pesan error di aplikasi

**Tidak bisa login:**
- Cek username dan password
- Pastikan tidak ada typo
- Hubungi admin untuk reset password

**Foto tidak bisa diupload:**
- Cek format file (harus JPG/PNG)
- Ukuran file tidak terlalu besar (max 10MB)
- Coba upload satu per satu

## Kontak

Untuk bantuan lebih lanjut, hubungi:
- Admin IT Riyadh Group
- Email: [email perusahaan]
- Phone: [nomor kontak]
