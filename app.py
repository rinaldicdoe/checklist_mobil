import streamlit as st
import datetime
import gspread
from google.oauth2.service_account import Credentials
import json
import os
from PIL import Image
import io
import base64

# ==========================================
# PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(
    page_title="Checklist Mobil - Riyadh Group",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk styling - Design hijau modern & user-friendly
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    /* Global Styling */
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    .main > div {
        padding-top: 1rem;
        background: linear-gradient(135deg, #f0f9f0 0%, #e8f5e9 100%);
    }
    
    /* Header App */
    h1 {
        color: #1b5e20 !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2, h3, h4, h5, h6 {
        color: #1b5e20 !important;
        font-weight: 600 !important;
    }
    
    /* Specific text styling - avoid breaking Streamlit internal elements */
    .main p {
        color: #1b5e20;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        font-weight: 600;
        font-size: 1.1em;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    /* Primary Button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%) !important;
        color: white !important;
    }
    
    /* Secondary Button */
    .stButton > button[kind="secondary"] {
        background: linear-gradient(135deg, #66bb6a 0%, #4CAF50 100%) !important;
        color: white !important;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 12px;
        font-size: 1.05em;
        transition: all 0.3s ease;
        background: #ffffff !important;
        color: #1b5e20 !important;
        font-weight: 500;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #2e7d32;
        box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.2);
    }
    
    /* Input labels */
    .stTextInput > label,
    .stTextArea > label {
        color: #1b5e20 !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
    }
    
    /* Radio Buttons - Besar & Jelas dengan Kontras Tinggi */
    .stRadio > label {
        font-size: 1.15em;
        font-weight: 600;
        color: #1b5e20 !important;
        margin-bottom: 8px;
        text-shadow: 0 1px 2px rgba(255,255,255,0.8);
    }
    
    .stRadio > div {
        gap: 15px;
        flex-wrap: wrap;
    }
    
    .stRadio > div > label {
        background: white;
        padding: 14px 28px;
        border-radius: 12px;
        border: 3px solid #4CAF50;
        font-size: 1.15em;
        font-weight: 700;
        color: #1b5e20 !important;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        min-width: 100px;
        text-align: center;
    }
    
    .stRadio > div > label:hover {
        border-color: #2e7d32;
        background: #e8f5e9;
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .stRadio > div > label[data-checked="true"] {
        background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%);
        color: white !important;
        border-color: #1b5e20;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.4);
    }
    
    /* Step Header - Hijau Gradient */
    .step-header {
        background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%);
        padding: 1.5rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 16px rgba(76, 175, 80, 0.3);
    }
    
    .step-header h2 {
        color: white !important;
        margin: 0 !important;
        font-weight: 600 !important;
        font-size: 1.8em !important;
    }
    
    /* Expander - Lebih Jelas dengan Kontras */
    div[data-testid="stExpander"] {
        background: white;
        border: 3px solid #4CAF50;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stExpander"]:hover {
        border-color: #2e7d32;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    div[data-testid="stExpander"] summary {
        padding: 1rem 1.2rem !important;
        background: #f1f8f4;
        border-radius: 12px;
        line-height: 1.5 !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #1b5e20 !important;
    }
    
    /* Hide arrow SVG */
    div[data-testid="stExpander"] summary svg {
        display: none !important;
    }
    
    /* Hide keyboard_arrow text specifically */
    div[data-testid="stExpander"] summary::before {
        content: none !important;
    }
    
    div[data-testid="stExpander"] summary * {
        font-family: inherit !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #81c784 100%);
        height: 12px;
        border-radius: 10px;
    }
    
    .progress-text {
        font-size: 1.4em;
        font-weight: 700;
        text-align: center;
        color: #1b5e20;
        margin: 1rem 0;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Success/Error Messages - Lebih Besar */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 12px;
        padding: 1rem 1.5rem;
        font-size: 1.1em;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #4CAF50;
        color: #1b5e20 !important;
    }
    
    .stSuccess * {
        color: #1b5e20 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-left: 5px solid #f44336;
        color: #c62828 !important;
    }
    
    .stError * {
        color: #c62828 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
        border-left: 5px solid #ff9800;
        color: #e65100 !important;
    }
    
    .stWarning * {
        color: #e65100 !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 5px solid #2196f3;
        color: #0d47a1 !important;
    }
    
    .stInfo * {
        color: #0d47a1 !important;
    }
    
    /* File Uploader */
    .stFileUploader {
        border: 2px dashed #4CAF50;
        border-radius: 15px;
        padding: 2rem;
        background: linear-gradient(135deg, #f1f8f4 0%, #e8f5e9 100%);
    }
    
    .stFileUploader > label {
        color: #1b5e20 !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
    }
    
    .stFileUploader section {
        color: #2e7d32 !important;
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent 0%, #81c784 50%, transparent 100%);
    }
    
    /* Cards Effect */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }
    
    /* Date/Time Input */
    .stDateInput, .stTimeInput {
        background: white;
        border-radius: 10px;
    }
    
    /* Tooltip */
    [data-baseweb="tooltip"] {
        background: #2e7d32 !important;
        border-radius: 8px;
        font-size: 1em;
    }
    
    /* ============================================ */
    /* RESPONSIVE DESIGN - MOBILE OPTIMIZATION */
    /* ============================================ */
    
    @media only screen and (max-width: 768px) {
        /* Reduce padding on mobile */
        .main > div {
            padding: 0.5rem !important;
        }
        
        /* Header text smaller on mobile */
        h1 {
            font-size: 1.8em !important;
        }
        
        h2 {
            font-size: 1.5em !important;
        }
        
        /* Step header responsive */
        .step-header h2 {
            font-size: 1.4em !important;
        }
        
        /* Radio buttons stack vertically on mobile */
        .stRadio > div {
            flex-direction: column !important;
            gap: 10px !important;
        }
        
        .stRadio > div > label {
            width: 100% !important;
            padding: 16px 20px !important;
            font-size: 1.2em !important;
        }
        
        .stRadio > label {
            font-size: 1.1em !important;
        }
        
        /* Expander title smaller on mobile */
        div[data-testid="stExpander"] summary {
            font-size: 1.05em !important;
            padding: 1rem !important;
            line-height: 1.4 !important;
        }
        
        /* Buttons full width on mobile */
        .stButton > button {
            font-size: 1.05em !important;
            padding: 14px !important;
        }
        
        /* Text inputs */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            font-size: 1em !important;
        }
        
        /* Columns stack on mobile */
        [data-testid="column"] {
            width: 100% !important;
            margin-bottom: 1rem;
        }
        
        /* Progress text */
        .progress-text {
            font-size: 1.1em !important;
        }
        
        /* Info boxes */
        .stSuccess, .stError, .stWarning, .stInfo {
            font-size: 1em !important;
            padding: 0.8rem 1rem !important;
        }
        
        /* File uploader */
        .stFileUploader {
            padding: 1rem !important;
        }
        
        /* Custom cards */
        div[style*="padding: 1.5rem"] {
            padding: 1rem !important;
            font-size: 0.95em !important;
        }
        
        /* Reduce box shadows on mobile */
        .stButton > button,
        div[data-testid="stExpander"],
        .step-header {
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }
    }
    
    /* Extra small devices (phones in portrait, less than 576px) */
    @media only screen and (max-width: 576px) {
        h1 {
            font-size: 1.5em !important;
        }
        
        .step-header h2 {
            font-size: 1.2em !important;
        }
        
        .stRadio > div > label {
            font-size: 1.1em !important;
            padding: 14px 16px !important;
        }
        
        div[data-testid="stExpander"] summary {
            font-size: 0.95em !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# KONFIGURASI & LOGIN
# ==========================================

# Daftar pengemudi (bisa dipindah ke database atau file eksternal)
USERS = {
    "admin": "admin123",
    "driver1": "pass1",
    "driver2": "pass2",
    "driver3": "pass3"
}

# Fungsi login dengan design menarik
def login_page():
    # Background effect
    st.markdown("""
    <style>
        .login-container {
            max-width: 500px;
            margin: 3rem auto;
            padding: 3rem;
            background: white;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%); 
                    padding: 2rem; border-radius: 20px; box-shadow: 0 8px 16px rgba(76, 175, 80, 0.3);">
            <h1 style="color: white; margin: 0; font-size: 2.5em;">🚗</h1>
            <h1 style="color: white; margin: 0.5rem 0 0 0;">Checklist Mobil</h1>
            <p style="color: #e8f5e9; margin: 0.5rem 0 0 0; font-size: 1.2em;">Riyadh Group</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #2e7d32; margin-bottom: 2rem;'>🔐 Login</h2>", unsafe_allow_html=True)
    
    username = st.text_input("👤 Username", placeholder="Masukkan username Anda")
    password = st.text_input("🔒 Password", type="password", placeholder="Masukkan password Anda")
    
    st.write("")  # spacing
    
    if st.button("🚀 MASUK", type="primary", use_container_width=True):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("✅ Login berhasil! Menuju aplikasi...")
            st.rerun()
        else:
            st.error("❌ Username atau password salah! Silakan coba lagi.")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                padding: 1.2rem; border-radius: 12px; border-left: 5px solid #2196f3;
                margin-top: 2rem;">
        <p style="margin: 0; text-align: center; color: #0d47a1; font-size: 1.05em;">
            💡 <strong>Login Default:</strong><br>
            Username: <code style="background: white; padding: 2px 8px; border-radius: 5px;">admin</code> 
            Password: <code style="background: white; padding: 2px 8px; border-radius: 5px;">admin123</code>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Cek status login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
    st.stop()

# Header dengan design menarik
col1, col2 = st.columns([5, 1])
with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%); 
                padding: 2rem; border-radius: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.2);">
        <h1 style="color: white; margin: 0; font-size: 2.5em;">🚗 Checklist Pemeriksaan Mobil</h1>
        <p style="color: #e8f5e9; font-size: 1.2em; margin: 0.5rem 0 0 0;">Riyadh Group - Sistem Digital</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.write("")  # spacing
    st.write("")  # spacing
    if st.button("🚪 Keluar", type="secondary", use_container_width=True):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()

st.write("")  # spacing

# User info badge dengan design
st.markdown(f"""
<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
            padding: 1rem; border-radius: 15px; border-left: 5px solid #4CAF50;
            margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <p style="margin: 0; font-size: 1.2em; font-weight: 600; color: #2e7d32;">
        👤 Login sebagai: <span style="color: #1b5e20;">{st.session_state['username']}</span>
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Initialize session state for tracking progress
if "checklist_data" not in st.session_state:
    st.session_state["checklist_data"] = {}

# ==========================================
# IDENTITAS - STEP 1
# ==========================================
st.markdown('<div class="step-header"><h2>📋 LANGKAH 1: Isi Identitas Anda</h2></div>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1em; color: #555; margin-bottom: 1rem;'>Lengkapi data pengemudi dan kendaraan di bawah ini:</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    nama = st.text_input("👤 Nama Pengemudi", value=st.session_state['username'], help="Nama akan otomatis terisi dari akun login")
    tanggal = st.date_input("📅 Tanggal Pemeriksaan", datetime.date.today())
with col2:
    nomor_kendaraan = st.text_input("🚙 Nomor Kendaraan", placeholder="Contoh: B 1234 XYZ", help="Masukkan nomor polisi kendaraan")
    waktu = st.time_input("🕐 Waktu Pemeriksaan")

# Validation
if nama and nomor_kendaraan:
    st.success("✅ Identitas lengkap!")
else:
    st.warning("⚠️ Mohon lengkapi nama dan nomor kendaraan")

st.divider()


# ==========================================
# DATA CHECKLIST (HASIL EKSTRAK DARI EXCEL)
# ==========================================

checklist = {
    "1. SEBELUM PEMERIKSAAN": [
        "Pasang safety traffic cone di depan mobil sebagai tanda mobil tidak bisa dijalankan"
    ],
    "2. DOKUMEN & LEGALITAS": [
        "STNK tersedia & masih berlaku",
        "SIM pengemudi sesuai & masih berlaku",
        "Buku servis/riwayat"
    ],
    "3. KONDISI EKSTERIOR": [
        "Body mobil aman",
        "Kaca tidak retak",
        "Wiper berfungsi",
        "Spion normal",
        "Ban tidak botak",
        "Tekanan angin sesuai",
        "Ban cadangan siap",
        "Lampu depan berfungsi",
        "Lampu sen berfungsi",
        "Lampu rem & belakang berfungsi",
        "Lampu hazard berfungsi"
    ],
    "4. KONDISI INTERIOR": [
        "Kabin bersih",
        "Indicator normal",
        "Sabuk pengaman",
        "AC normal",
        "Klakson berfungsi",
        "Power window normal"
    ],
    "5. MESIN & CAIRAN": [
        "Oli mesin cukup",
        "Air radiator cukup",
        "Air wiper cukup",
        "Minyak rem cukup",
        "Aki baik",
        "Tidak ada kebocoran"
    ],
    "6. BAHAN BAKAR": [
        "Minimal ½ tank",
        "Tidak ada bau bensin"
    ],
    "7. REM & KEMUDI": [
        "Rem utama baik",
        "Rem tangan baik",
        "Setir stabil",
        "Suspensi normal"
    ],
    "8. KELENGKAPAN": [
        "Dongkrak & kunci roda",
        "Segitiga pengaman",
        "P3K",
        "APAR"
    ],
    "9. PEMERIKSAAN SEBELUM JALAN": [
        "Pastikan pintu belakang, samping, dan depan tertutup",
        "Pindahkan safety traffic cone di depan mobil ke dalam mobil area belakang"
    ],
    "10. UJI JALAN": [
        "Akselerasi normal",
        "Pengereman halus",
        "Tidak ada getaran",
        "Transmisi smooth"
    ]
}

# dictionary untuk menampung jawaban user
hasil = {}

# Icon mapping
section_icons = {
    "1. SEBELUM PEMERIKSAAN": "📋",
    "2. DOKUMEN & LEGALITAS": "📄",
    "3. KONDISI EKSTERIOR": "🚗",
    "4. KONDISI INTERIOR": "🪑",
    "5. MESIN & CAIRAN": "⚙️",
    "6. BAHAN BAKAR": "⛽",
    "7. REM & KEMUDI": "🛞",
    "8. KELENGKAPAN": "🧰",
    "9. PEMERIKSAAN SEBELUM JALAN": "🚦",
    "10. UJI JALAN": "🏁"
}

# ==========================================
# RENDER CHECKLIST - STEP 2
# ==========================================
st.markdown('<div class="step-header"><h2>✅ LANGKAH 2: Periksa Kondisi Kendaraan</h2></div>', unsafe_allow_html=True)

# Calculate progress
total_items = sum(len(items) for items in checklist.values())
completed_items = 0

# Count completed items and create progress data
section_progress_data = []
for section, items in checklist.items():
    section_completed = sum(1 for item in items if f"{section}_{item}" in st.session_state)
    completed_items += section_completed
    section_progress_data.append({
        'section': section,
        'completed': section_completed,
        'total': len(items),
        'percentage': (section_completed / len(items) * 100) if len(items) > 0 else 0
    })

# Overall progress bar at the top
overall_progress = (completed_items / total_items * 100) if total_items > 0 else 0
progress_color = "#4CAF50" if overall_progress == 100 else "#ff9800" if overall_progress >= 50 else "#2196F3"

st.markdown(f"""
<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
            padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h3 style="margin: 0; color: #1565c0;">📊 Progress Keseluruhan</h3>
        <span style="font-size: 1.5em; font-weight: bold; color: {progress_color};">
            {completed_items}/{total_items}
        </span>
    </div>
    <div style="background: #e0e0e0; height: 25px; border-radius: 12px; overflow: hidden;">
        <div style="background: {progress_color}; width: {overall_progress}%; height: 100%; 
                    transition: width 0.3s ease; display: flex; align-items: center; justify-content: center;
                    color: white; font-weight: bold; font-size: 0.9em;">
            {overall_progress:.0f}%
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Progress cards for each section - compact version
section_summary = []
for data in section_progress_data:
    status_emoji = "✅" if data['percentage'] == 100 else "🔄" if data['percentage'] > 0 else "⭕"
    section_summary.append(f"{status_emoji} {data['completed']}/{data['total']}")

st.markdown(f"""
<div style="background: white; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
    <div style="font-size: 0.9em; color: #666; margin-bottom: 0.5rem;">📋 Progress Per Section:</div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 0.5rem;">
        {' '.join([f'<div style="background: #f5f5f5; padding: 0.4rem; border-radius: 6px; text-align: center; font-size: 0.85em;">{item}</div>' for item in section_summary])}
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Initialize current tab index in session state
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = 0

# Create tabs for each section
tab_names = []
for section, items in checklist.items():
    section_completed = sum(1 for item in items if f"{section}_{item}" in st.session_state)
    status_icon = "✅" if section_completed == len(items) else "🔄" if section_completed > 0 else "⭕"
    tab_names.append(f"{status_icon} {section.split('. ')[1] if '. ' in section else section}")

tabs = st.tabs(tab_names)

# Render each section in its tab
for tab_idx, (section, items) in enumerate(checklist.items()):
    with tabs[tab_idx]:
        hasil[section] = {}
        
        # Section header with progress
        section_completed = sum(1 for item in items if f"{section}_{item}" in st.session_state)
        section_pct = (section_completed / len(items) * 100) if len(items) > 0 else 0
        
        # Section progress indicator
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #f1f8f4 0%, #e8f5e9 100%); 
                    padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin: 0; color: #2e7d32;">📝 {section}</h4>
                <span style="font-weight: bold; color: #1b5e20;">
                    {section_completed}/{len(items)} items
                </span>
            </div>
            <div style="background: #c8e6c9; height: 8px; border-radius: 4px; margin-top: 0.8rem; overflow: hidden;">
                <div style="background: #4caf50; width: {section_pct}%; height: 100%; transition: width 0.3s ease;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Render items
        for idx, item in enumerate(items):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                hasil[section][item] = st.radio(
                    item,
                    ["Ya", "Tidak"],
                    horizontal=True,
                    key=f"{section}_{item}",
                    label_visibility="visible"
                )
            
            with col2:
                # Visual indicator
                if f"{section}_{item}" in st.session_state:
                    if st.session_state[f"{section}_{item}"] == "Ya":
                        st.success("✓")
                    else:
                        st.error("✗")
        
        # Section completion message
        if section_completed == len(items):
            st.success(f"🎯 Section ini sudah lengkap! Lanjut ke section berikutnya.")
        
        # Navigation buttons
        st.markdown("<br>", unsafe_allow_html=True)
        nav_cols = st.columns([1, 2, 1])
        
        with nav_cols[0]:
            if tab_idx > 0:
                prev_section = list(checklist.keys())[tab_idx - 1]
                prev_name = prev_section.split('. ')[1] if '. ' in prev_section else prev_section
                if st.button(f"⬅️ {prev_name[:20]}", key=f"prev_{tab_idx}", use_container_width=True):
                    st.session_state.current_tab = tab_idx - 1
                    st.rerun()
        
        with nav_cols[2]:
            if tab_idx < len(checklist) - 1:
                next_section = list(checklist.keys())[tab_idx + 1]
                next_name = next_section.split('. ')[1] if '. ' in next_section else next_section
                if st.button(f"{next_name[:20]} ➡️", key=f"next_{tab_idx}", use_container_width=True):
                    st.session_state.current_tab = tab_idx + 1
                    st.rerun()

# Overall progress dengan design menarik
st.divider()

# Progress container
progress_percentage = (completed_items / total_items) * 100 if total_items > 0 else 0
progress_color = "#4CAF50" if progress_percentage == 100 else "#ff9800" if progress_percentage >= 50 else "#f44336"
progress_emoji = "🎉" if progress_percentage == 100 else "📊" if progress_percentage >= 50 else "📝"

st.markdown(f"""
<div style="background: white; padding: 1.5rem; border-radius: 15px; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 1.5rem 0;">
    <p style="text-align: center; font-size: 1.1em; color: #666; margin: 0 0 0.5rem 0;">
        Progress Checklist {progress_emoji}
    </p>
    <h2 style="text-align: center; color: {progress_color}; margin: 0;">
        {completed_items} / {total_items} Items ({progress_percentage:.0f}%)
    </h2>
</div>
""", unsafe_allow_html=True)

st.progress(progress_percentage / 100)

st.divider()

# ==========================================
# UPLOAD FOTO & CATATAN - STEP 3
# ==========================================
st.markdown('<div class="step-header"><h2>📷 LANGKAH 3: Dokumentasi (Opsional)</h2></div>', unsafe_allow_html=True)

# Create tabs for documentation
doc_tabs = st.tabs(["📸 Upload Foto", "📝 Catatan Tambahan"])

# Tab 1: Upload Foto
with doc_tabs[0]:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
        <p style="margin: 0; font-size: 1.1em; color: #1565c0;">
            📸 <strong>Upload foto kondisi kendaraan untuk dokumentasi lengkap</strong><br>
            <span style="font-size: 0.95em; color: #424242;">
            Opsional - Bisa upload multiple foto sekaligus
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "Pilih foto (JPG, JPEG, PNG)", 
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        help="Klik 'Browse files' untuk memilih foto dari komputer Anda"
    )
    
    # Simpan info foto
    foto_info = []
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} foto berhasil diupload")
        
        # Display photos in grid
        num_cols = min(3, len(uploaded_files))
        cols = st.columns(num_cols)
        
        for idx, uploaded_file in enumerate(uploaded_files):
            with cols[idx % num_cols]:
                image = Image.open(uploaded_file)
                st.image(image, caption=f"📸 {uploaded_file.name}", use_container_width=True)
                # Simpan info foto untuk dikirim ke Google Sheets
                foto_info.append({
                    "nama_file": uploaded_file.name,
                    "ukuran": uploaded_file.size
                })
    else:
        st.info("💡 Belum ada foto yang diupload (opsional)")

# Tab 2: Catatan
with doc_tabs[1]:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f1f8f4 0%, #e8f5e9 100%); 
                padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
        <p style="margin: 0; font-size: 1.1em; color: #2e7d32;">
            📝 <strong>Tambahkan catatan detail tentang kondisi kendaraan</strong><br>
            <span style="font-size: 0.95em; color: #424242;">
            Opsional - Jelaskan kondisi khusus, kerusakan, atau hal yang perlu perhatian
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    catatan = st.text_area(
        "Tulis catatan di sini",
        height=200,
        placeholder="Contoh:\n• Ban depan kiri perlu diganti segera, tekanan angin kurang\n• AC kurang dingin di bagian belakang\n• Lampu sein kanan agak redup\n• Oli mesin sudah waktunya ganti\n• Kaca spion kiri retak kecil",
        help="Jelaskan kondisi khusus, kerusakan, atau hal yang perlu perhatian"
    )
    
    if catatan:
        word_count = len(catatan.split())
        st.success(f"✅ Catatan ditambahkan ({len(catatan)} karakter, ~{word_count} kata)")
        
        # Preview catatan
        with st.container():
            st.markdown("""
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50; margin-top: 1rem;">
                <strong style="color: #2e7d32;">Preview Catatan:</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write(catatan)
    else:
        st.info("💡 Belum ada catatan (opsional)")

st.divider()


# ==========================================
# FUNGSI GOOGLE SHEETS
# ==========================================
def upload_to_imgbb(uploaded_file, api_key=""):
    """
    Upload foto ke ImgBB (free image hosting) dan return link
    Jika tidak ada API key, return base64
    """
    import requests
    
    try:
        if api_key:
            # Upload to ImgBB
            uploaded_file.seek(0)
            files = {'image': uploaded_file.read()}
            response = requests.post(
                f"https://api.imgbb.com/1/upload?key={api_key}",
                files=files
            )
            if response.status_code == 200:
                return response.json()['data']['url']
        
        # Fallback: return base64 data URL (bisa ditampilkan di browser)
        uploaded_file.seek(0)
        img_data = uploaded_file.read()
        img_base64 = base64.b64encode(img_data).decode()
        return f"data:{uploaded_file.type};base64,{img_base64[:100]}..." # shortened untuk sheets
    except Exception as e:
        return f"Error: {str(e)}"

def save_photos_to_separate_sheet(uploaded_files, sheet_name, creds):
    """
    Simpan foto ke sheet terpisah dalam spreadsheet yang sama
    Return list of row numbers untuk referensi
    """
    try:
        client = gspread.authorize(creds)
        SPREADSHEET_NAME = "Checklist Mobil Riyadh"
        spreadsheet = client.open(SPREADSHEET_NAME)
        
        # Get or create "Foto" sheet
        try:
            foto_sheet = spreadsheet.worksheet("Foto")
        except:
            foto_sheet = spreadsheet.add_worksheet(title="Foto", rows="1000", cols="10")
            # Add header
            foto_sheet.append_row(["Timestamp", "Nomor Kendaraan", "Nama File", "Ukuran (KB)", "Link/Preview"])
        
        photo_links = []
        for uploaded_file in uploaded_files:
            # Create mini preview link using base64
            uploaded_file.seek(0)
            img_data = uploaded_file.read()
            
            # Compress image untuk preview
            from PIL import Image
            import io
            uploaded_file.seek(0)
            img = Image.open(uploaded_file)
            
            # Resize untuk thumbnail
            img.thumbnail((200, 200))
            buffer = io.BytesIO()
            img.save(buffer, format=img.format or 'JPEG')
            buffer.seek(0)
            
            # Create viewable link using Google Sheets formula
            img_base64 = base64.b64encode(buffer.read()).decode()
            preview_link = f"data:image/jpeg;base64,{img_base64}"
            
            # Add to foto sheet
            row_data = [
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                sheet_name,
                uploaded_file.name,
                round(uploaded_file.size / 1024, 2),
                preview_link[:50000] if len(preview_link) < 50000 else preview_link[:50000] + "..."  # Google Sheets cell limit
            ]
            foto_sheet.append_row(row_data)
            
            # Create reference
            row_num = len(foto_sheet.get_all_values())
            photo_links.append(f"Foto!A{row_num}")
        
        return photo_links
    except Exception as e:
        st.warning(f"⚠️ Foto tidak bisa disimpan ke sheet terpisah: {str(e)}")
        return []

def send_to_google_sheets(data, uploaded_files=None):
    """
    Kirim data ke Google Sheets dengan format terstruktur
    Upload foto ke Google Drive jika ada
    """
    try:
        # Path ke file credentials (download dari Google Cloud Console)
        credentials_file = "credentials.json"
        
        if not os.path.exists(credentials_file):
            st.warning("⚠️ File credentials.json tidak ditemukan. Data tidak dikirim ke Google Sheets.")
            st.info("""
            **Cara setup Google Sheets API:**
            1. Buka Google Cloud Console
            2. Buat project baru atau pilih yang ada
            3. Enable Google Sheets API & Google Drive API
            4. Buat Service Account & download JSON credentials
            5. Simpan sebagai 'credentials.json' di folder aplikasi
            6. Share Google Sheet ke email service account
            """)
            return False
        
        # Setup credentials
        SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
        client = gspread.authorize(creds)
        
        # Save photos to separate sheet and get references
        photo_references = []
        if uploaded_files and len(uploaded_files) > 0:
            folder_id = f"{data['nomor_kendaraan']}_{data['tanggal']}"
            with st.spinner("📤 Menyimpan foto..."):
                photo_references = save_photos_to_separate_sheet(uploaded_files, folder_id, creds)
        
        photo_summary = ", ".join(photo_references) if photo_references else "-"
        
        # Buka spreadsheet
        SPREADSHEET_NAME = "Checklist Mobil Riyadh"
        sheet = client.open(SPREADSHEET_NAME).sheet1
        
        # Check if header exists, if not create it
        if sheet.row_count == 0 or sheet.row_values(1) == []:
            # Create header row
            header = [
                "Timestamp", "Nama Pengemudi", "Nomor Kendaraan", "Tanggal", "Waktu"
            ]
            
            # Add all checklist items as columns
            for section, items in data["hasil"].items():
                for item in items.keys():
                    header.append(f"{section} - {item}")
            
            header.extend(["Catatan", "Jumlah Foto", "Referensi Foto (lihat sheet 'Foto')"])
            sheet.append_row(header)
        
        # Prepare row data
        row = [
            data["timestamp"],
            data["nama"],
            data["nomor_kendaraan"],
            data["tanggal"],
            data["waktu"]
        ]
        
        # Add checklist results (Ya/Tidak for each item)
        for section, items in data["hasil"].items():
            for item, jawaban in items.items():
                row.append(jawaban)
        
        # Add notes, photo count, and photo references
        row.append(data["catatan"] if data["catatan"] else "-")
        row.append(len(photo_references))
        row.append(photo_summary)
        
        # Append data to sheet
        sheet.append_row(row)
        
        return True
    except Exception as e:
        st.error(f"❌ Gagal mengirim ke Google Sheets: {str(e)}")
        return False

# ==========================================
# SUBMIT - STEP 4
# ==========================================
st.markdown('<div class="step-header"><h2>🚀 LANGKAH 4: Kirim Data</h2></div>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1em; color: #555; margin-bottom: 1rem;'>Periksa kembali data Anda sebelum mengirim:</p>", unsafe_allow_html=True)

# Pre-submit validation & summary dengan card design
st.markdown("""
<div style="background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%); 
            padding: 1.5rem; border-radius: 15px; border: 3px solid #ffc107;
            margin-bottom: 1.5rem; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <p style="text-align: center; font-size: 1.3em; font-weight: 600; color: #f57c00; margin: 0;">
        ⚠️ Periksa Kelengkapan Data Sebelum Submit
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if nama and nomor_kendaraan:
        st.markdown("""
        <div style="background: #e8f5e9; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #4CAF50;">
            <p style="margin: 0; font-size: 1.1em; font-weight: 600; color: #2e7d32;">✅ Identitas Lengkap</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #ffebee; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #f44336;">
            <p style="margin: 0; font-size: 1.1em; font-weight: 600; color: #c62828;">❌ Identitas Belum Lengkap</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if completed_items == total_items:
        st.markdown(f"""
        <div style="background: #e8f5e9; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #4CAF50;">
            <p style="margin: 0; font-size: 1.1em; font-weight: 600; color: #2e7d32;">✅ Checklist Lengkap<br>({total_items} items)</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: #fff3e0; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #ff9800;">
            <p style="margin: 0; font-size: 1.1em; font-weight: 600; color: #e65100;">⚠️ Checklist<br>{completed_items}/{total_items} items</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    optional_count = 0
    if uploaded_files:
        optional_count += 1
    if catatan:
        optional_count += 1
    st.markdown(f"""
    <div style="background: #e3f2fd; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #2196f3;">
        <p style="margin: 0; font-size: 1.1em; font-weight: 600; color: #1565c0;">📎 Tambahan<br>{optional_count}/2 (opsional)</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")  # spacing

# Submit button dengan kondisi
can_submit = nama and nomor_kendaraan

if can_submit:
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0;">
        <p style="font-size: 1.15em; color: #2e7d32; font-weight: 600;">
            ✓ Siap untuk submit! Klik tombol di bawah ini:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✅ KIRIM DATA SEKARANG", type="primary", use_container_width=True):
        
        with st.spinner("⏳ Menyimpan data..."):
            # Prepare data
            data = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "nama": nama,
                "nomor_kendaraan": nomor_kendaraan,
                "tanggal": str(tanggal),
                "waktu": str(waktu),
                "hasil": hasil,
                "catatan": catatan,
                "foto_info": foto_info
            }
            
            # Kirim ke Google Sheets (dengan foto jika ada)
            sheets_success = send_to_google_sheets(data, uploaded_files)
        
        # Success message
        st.balloons()
        st.success("🎉 **Checklist berhasil disimpan!**")
        
        if sheets_success:
            st.success("✅ Data berhasil dikirim ke Google Sheets!")
            if uploaded_files and len(uploaded_files) > 0:
                st.info("📸 Info foto tersimpan di Google Sheets (foto asli tetap di lokal)")
        
        # Tampilkan ringkasan dalam card style
        st.write("---")
        st.subheader("📌 Ringkasan Pemeriksaan")
        
        # Info cards
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"""
            **👤 Pengemudi:** {nama}  
            **🚙 No. Kendaraan:** {nomor_kendaraan}
            """)
        with col2:
            st.info(f"""
            **📅 Tanggal:** {tanggal}  
            **🕐 Waktu:** {waktu}
            """)
        
        if catatan:
            with st.expander("Catatan"):
                st.write(catatan)
        
        if foto_info:
            with st.expander(f"Foto ({len(foto_info)} file)"):
                for foto in foto_info:
                    st.write(f"• {foto['nama_file']} ({foto['ukuran']} bytes)")

        st.write("---")
        
        # Hasil checklist dengan styling
        st.subheader("Hasil Pemeriksaan Detail")
        
        for section, items in hasil.items():
            # Count Ya/Tidak
            ya_count = sum(1 for jawaban in items.values() if jawaban == "Ya")
            tidak_count = len(items) - ya_count
            
            with st.expander(f"{section} ({ya_count} Ya, {tidak_count} Tidak)"):
                for item, jawaban in items.items():
                    if jawaban == "Ya":
                        st.success(f"✅ {item}")
                    else:
                        st.error(f"❌ {item}")
        
        # Action buttons
        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📝 Isi Checklist Baru", use_container_width=True):
                st.rerun()
        with col2:
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state["logged_in"] = False
                st.rerun()
else:
    st.markdown("""
    <div style="background: #ffebee; padding: 1.5rem; border-radius: 15px; 
                border-left: 5px solid #f44336; text-align: center; margin: 1rem 0;">
        <p style="margin: 0; font-size: 1.2em; font-weight: 600; color: #c62828;">
            ❌ Tidak Bisa Submit!<br>
            <span style="font-size: 0.9em;">Pastikan <strong>Nama</strong> dan <strong>Nomor Kendaraan</strong> sudah diisi</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.button("✅ KIRIM DATA SEKARANG", type="primary", disabled=True, use_container_width=True)
