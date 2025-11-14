#!/bin/bash

echo "🚗 ====================================="
echo "   Instalasi Checklist Mobil - Riyadh"
echo "   ====================================="
echo ""

# Check Python version
echo "📌 Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 tidak ditemukan. Install Python 3 terlebih dahulu."
    exit 1
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Instalasi dependencies gagal."
    exit 1
fi

echo ""
echo "✅ Instalasi selesai!"
echo ""
echo "🚀 Untuk menjalankan aplikasi:"
echo "   streamlit run app.py"
echo ""
echo "🔑 Login default:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "📖 Baca dokumentasi:"
echo "   - QUICKSTART.md (panduan cepat)"
echo "   - PANDUAN_PENGGUNA.md (manual lengkap)"
echo "   - SETUP_GOOGLE_SHEETS.md (setup sheets)"
echo ""
echo "Selamat menggunakan! 🎉"
