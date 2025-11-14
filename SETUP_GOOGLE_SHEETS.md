# Setup Google Sheets API

Ikuti langkah-langkah berikut untuk mengaktifkan integrasi Google Sheets:

## 1. Buat Project di Google Cloud Console

1. Kunjungi [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru atau pilih project yang sudah ada
3. Berikan nama project (contoh: "Checklist Mobil Riyadh")

## 2. Enable Google Sheets API

1. Di Google Cloud Console, buka menu **APIs & Services** > **Enable APIs and Services**
2. Cari "Google Sheets API"
3. Klik dan enable API tersebut
4. Ulangi untuk "Google Drive API" (opsional tapi direkomendasikan)

## 3. Buat Service Account

1. Buka **APIs & Services** > **Credentials**
2. Klik **Create Credentials** > **Service Account**
3. Berikan nama service account (contoh: "checklist-bot")
4. Klik **Create and Continue**
5. Pilih role **Editor** atau **Owner**
6. Klik **Done**

## 4. Download Credentials JSON

1. Di halaman Credentials, klik service account yang baru dibuat
2. Buka tab **Keys**
3. Klik **Add Key** > **Create New Key**
4. Pilih format **JSON**
5. File akan otomatis terdownload
6. **Rename file menjadi `credentials.json`**
7. **Copy file ke folder aplikasi** (folder yang sama dengan `app.py`)

## 5. Buat & Setup Google Sheet

1. Buka [Google Sheets](https://sheets.google.com/)
2. Buat spreadsheet baru
3. Beri nama: **"Checklist Mobil Riyadh"** (atau sesuai keinginan)
4. Di baris pertama (header), tambahkan kolom:
   - Timestamp
   - Nama Pengemudi
   - Nomor Kendaraan
   - Tanggal
   - Waktu
   - Hasil Checklist
   - Catatan
   - Info Foto

## 6. Share Sheet ke Service Account

1. Buka file `credentials.json` yang sudah didownload
2. Cari field `"client_email"` (contoh: `checklist-bot@project-id.iam.gserviceaccount.com`)
3. Copy email tersebut
4. Di Google Sheet, klik tombol **Share**
5. Paste email service account
6. Berikan permission **Editor**
7. Klik **Send**

## 7. Update Kode (jika perlu)

Jika nama spreadsheet berbeda, edit file `app.py` di bagian:

```python
SPREADSHEET_NAME = "Checklist Mobil Riyadh"  # Ganti dengan nama sheet Anda
```

## 8. Test Aplikasi

Jalankan aplikasi dan test submit checklist. Data harus otomatis masuk ke Google Sheet.

## Troubleshooting

### Error: File credentials.json tidak ditemukan
- Pastikan file `credentials.json` ada di folder yang sama dengan `app.py`
- Cek nama file, harus exact `credentials.json`

### Error: Permission denied
- Pastikan sudah share Google Sheet ke email service account
- Berikan permission Editor, bukan Viewer

### Error: Spreadsheet not found
- Cek nama spreadsheet di Google Sheets harus sama dengan variable `SPREADSHEET_NAME` di kode
- Atau gunakan ID spreadsheet (dari URL) sebagai gantinya

### Error: API not enabled
- Pastikan Google Sheets API sudah di-enable di Google Cloud Console
- Tunggu beberapa menit setelah enable API

## Keamanan

⚠️ **PENTING:**
- Jangan upload file `credentials.json` ke GitHub atau repository public
- Tambahkan `credentials.json` ke `.gitignore`
- Simpan file credentials di tempat yang aman
