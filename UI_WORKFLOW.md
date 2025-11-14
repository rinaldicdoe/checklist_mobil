# 🎨 Tampilan & Workflow Aplikasi

## 📱 Screenshots & Flow

### 1. Halaman Login
```
┌────────────────────────────────────────┐
│  🔐 Login - Form Ceklist Pemeriksaan  │
│           Riyadh Group                 │
├────────────────────────────────────────┤
│                                        │
│  Username: [________________]          │
│                                        │
│  Password: [________________]          │
│                                        │
│       [      Login      ]              │
│                                        │
│  💡 Default login: admin / admin123    │
│                                        │
└────────────────────────────────────────┘
```

**Fitur:**
- Simple username/password input
- Info login default
- Error message jika login gagal

---

### 2. Header & Info User
```
┌────────────────────────────────────────────────────────┐
│ Form Ceklist Pemeriksaan Mobil - Riyadh Group  [Logout]│
├────────────────────────────────────────────────────────┤
│ ℹ️  Login sebagai: admin                                │
└────────────────────────────────────────────────────────┘
```

---

### 3. Form Identitas
```
┌────────────────────────────────────────┐
│  Identitas Pengemudi                   │
├────────────────────────────────────────┤
│  Nama Pengemudi:                       │
│  [admin_________________________]      │
│                                        │
│  Nomor Kendaraan:                      │
│  [B_1234_XYZ____________________]      │
│                                        │
│  Tanggal Pemeriksaan: [📅 14/11/2025]  │
│  Waktu Pemeriksaan:   [🕐 10:30]       │
└────────────────────────────────────────┘
```

**Catatan:**
- Nama auto-fill dari username login
- Nomor kendaraan wajib diisi
- Tanggal default hari ini

---

### 4. Checklist Sections

#### Section: 1. SEBELUM PEMERIKSAAN
```
┌────────────────────────────────────────────────────────┐
│  1. SEBELUM PEMERIKSAAN                                │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Pasang safety traffic cone di depan mobil             │
│  ○ Ya    ○ Tidak                                       │
│                                                        │
│  STNK tersedia & masih berlaku                         │
│  ○ Ya    ○ Tidak                                       │
│                                                        │
│  SIM pengemudi sesuai & masih berlaku                  │
│  ○ Ya    ○ Tidak                                       │
│                                                        │
│  Buku servis/riwayat                                   │
│  ○ Ya    ○ Tidak                                       │
└────────────────────────────────────────────────────────┘
```

#### Section: 3. KONDISI EKSTERIOR
```
┌────────────────────────────────────────────────────────┐
│  3. KONDISI EKSTERIOR                                  │
├────────────────────────────────────────────────────────┤
│  Body mobil aman           ○ Ya  ○ Tidak               │
│  Kaca tidak retak          ○ Ya  ○ Tidak               │
│  Wiper berfungsi           ○ Ya  ○ Tidak               │
│  Spion normal              ○ Ya  ○ Tidak               │
│  Ban tidak botak           ○ Ya  ○ Tidak               │
│  Tekanan angin sesuai      ○ Ya  ○ Tidak               │
│  Ban cadangan siap         ○ Ya  ○ Tidak               │
│  Lampu depan berfungsi     ○ Ya  ○ Tidak               │
│  Lampu sen berfungsi       ○ Ya  ○ Tidak               │
│  Lampu rem & belakang      ○ Ya  ○ Tidak               │
│  Lampu hazard berfungsi    ○ Ya  ○ Tidak               │
└────────────────────────────────────────────────────────┘
```

*... dan seterusnya untuk semua sections*

---

### 5. Upload Foto
```
┌────────────────────────────────────────────────────────┐
│  📷 Upload Foto Kondisi Mobil                          │
├────────────────────────────────────────────────────────┤
│  Upload foto kondisi kendaraan (opsional, multiple)   │
│                                                        │
│  Pilih foto: [Browse files...]                         │
│                                                        │
│  ✅ 3 foto telah diupload                              │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │  [IMG 1] │  │  [IMG 2] │  │  [IMG 3] │            │
│  │   📷     │  │   📷     │  │   📷     │            │
│  │ban_dpn.jpg│ │mesin.jpg │  │interior.jpg           │
│  └──────────┘  └──────────┘  └──────────┘            │
└────────────────────────────────────────────────────────┘
```

**Fitur:**
- Multiple file upload
- Preview foto dalam grid 3 kolom
- Nama file ditampilkan
- Bisa upload JPG, JPEG, PNG

---

### 6. Catatan / Komentar
```
┌────────────────────────────────────────────────────────┐
│  📝 Catatan / Komentar                                 │
├────────────────────────────────────────────────────────┤
│  Tambahkan catatan atau komentar tambahan              │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │ Ban depan kiri tekanannya kurang, perlu        │   │
│  │ dipompa. AC kurang dingin di bagian belakang.  │   │
│  │ Lampu sein kanan agak redup.                   │   │
│  │                                                │   │
│  │                                                │   │
│  └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

### 7. Submit & Hasil
```
┌────────────────────────────────────────────────────────┐
│         [ ✅ Submit Checklist ]                         │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ✅ Checklist berhasil disimpan!                       │
│                                                        │
│  📤 Mengirim data ke Google Sheets...                  │
│  ✅ Data berhasil dikirim ke Google Sheets!            │
│                                                        │
│  ────────────────────────────────────────             │
│                                                        │
│  📌 Ringkasan Data:                                    │
│                                                        │
│  Nama:              admin                              │
│  Nomor Kendaraan:   B 1234 XYZ                         │
│  Tanggal:           2025-11-14                         │
│  Waktu:             10:30:00                           │
│  Catatan:           Ban depan kiri tekanannya...       │
│  Foto:              3 file terupload                   │
│                                                        │
│  ────────────────────────────────────────             │
│                                                        │
│  📋 Hasil Checklist:                                   │
│                                                        │
│  ▼ 1. SEBELUM PEMERIKSAAN                              │
│     ✅ Pasang safety traffic cone: Ya                  │
│     ✅ STNK tersedia & masih berlaku: Ya               │
│     ✅ SIM pengemudi sesuai: Ya                        │
│     ❌ Buku servis/riwayat: Tidak                      │
│                                                        │
│  ▼ 3. KONDISI EKSTERIOR                                │
│     ✅ Body mobil aman: Ya                             │
│     ✅ Kaca tidak retak: Ya                            │
│     ... dst ...                                        │
└────────────────────────────────────────────────────────┘
```

**Fitur Hasil:**
- Success message
- Status pengiriman Google Sheets
- Ringkasan data dalam 2 kolom
- Hasil per section dengan expander
- Icon ✅ untuk Ya, ❌ untuk Tidak

---

## 🔄 User Flow Diagram

```
START
  │
  ▼
┌─────────────┐
│   Login     │
│  (Username  │
│  Password)  │
└──────┬──────┘
       │ ✅ Valid
       ▼
┌─────────────────┐
│  Main Form      │
│  - Identitas    │
│  - Checklist    │
│  - Upload Foto  │
│  - Catatan      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Validasi Form  │
│  (Nama & Nomor  │
│   harus diisi)  │
└────────┬────────┘
         │ ✅ Valid
         ▼
┌─────────────────┐
│  Submit Data    │
└────────┬────────┘
         │
         ├──────────────┐
         │              │
         ▼              ▼
┌──────────────┐  ┌────────────┐
│ Google Sheets│  │  Display   │
│  (if setup)  │  │  Summary   │
└──────────────┘  └─────┬──────┘
                        │
                        ▼
                  ┌──────────┐
                  │  Logout  │
                  │    or    │
                  │  Repeat  │
                  └──────────┘
```

---

## 📊 Data Flow

```
USER INPUT
    │
    ├─ Identitas (nama, nomor, tanggal, waktu)
    ├─ Checklist (40+ items x Ya/Tidak)
    ├─ Foto (multiple files)
    └─ Catatan (text)
    │
    ▼
SESSION STATE
    │
    └─ logged_in: True
       username: "admin"
    │
    ▼
VALIDATION
    │
    ├─ Nama tidak kosong ✓
    └─ Nomor kendaraan tidak kosong ✓
    │
    ▼
PROCESSING
    │
    ├─ Format data ke dictionary
    ├─ Timestamp ditambahkan
    ├─ Foto info extracted
    └─ JSON untuk hasil checklist
    │
    ▼
OUTPUT
    │
    ├─ Display di UI (Streamlit)
    └─ Send to Google Sheets (optional)
        │
        ├─ Authenticate via credentials.json
        ├─ Open spreadsheet
        ├─ Format row data
        └─ Append to sheet
```

---

## 📱 Responsive Design Notes

Aplikasi Streamlit auto-responsive untuk:
- 💻 Desktop (1920x1080, 1366x768)
- 📱 Tablet (iPad, Android tablets)
- 📱 Mobile (dengan layout adjustments)

**Tips Mobile:**
- Radio buttons tetap horizontal untuk Ya/Tidak
- Foto preview adjust ke single column di mobile
- Text area tetap usable
- Sidebar collapse di mobile

---

## 🎨 Color & Style Guide

### Success States:
- ✅ Green checkmark untuk "Ya"
- Success banners: Green background

### Warning States:
- ⚠️ Yellow/Orange untuk warnings
- Info messages: Blue background

### Error States:
- ❌ Red X untuk "Tidak"
- Error messages: Red background

### Neutral:
- ℹ️ Blue info icon
- Gray for labels

---

## 🔔 User Feedback Elements

### Success:
```python
st.success("✅ Checklist berhasil disimpan!")
st.success("✅ Data berhasil dikirim ke Google Sheets!")
```

### Error:
```python
st.error("❌ Nama pengemudi dan nomor kendaraan harus diisi!")
st.error("❌ Gagal mengirim ke Google Sheets: ...")
```

### Warning:
```python
st.warning("⚠️ File credentials.json tidak ditemukan...")
```

### Info:
```python
st.info("💡 Default login: admin / admin123")
st.info(f"👤 Login sebagai: {username}")
```

---

## 📋 Checklist UX Best Practices

✅ **Good UX Implemented:**
- Auto-fill nama dari username
- Default tanggal hari ini
- Horizontal radio buttons (mudah klik)
- Visual feedback di setiap action
- Clear error messages
- Expandable results (tidak overwhelming)
- Logout button accessible

🔄 **Future Improvements:**
- Loading spinner saat submit
- Progress bar saat upload foto
- Confirm dialog sebelum logout
- Toast notifications
- Keyboard shortcuts
- Dark mode toggle

---

## 🎯 Accessibility Features

- ✅ Clear labels untuk semua inputs
- ✅ Logical tab order
- ✅ Visual feedback untuk actions
- ✅ Error messages yang descriptive
- ⏳ Screen reader support (future)
- ⏳ Keyboard-only navigation (future)

---

*Dokumentasi ini menjelaskan tampilan dan workflow aplikasi secara visual.*
