# aplikasi_utama.py
import streamlit as st
from datetime import datetime
from model_data import Tabungan
from fungsi_pendukung import tambah_latar_belakang
from halaman import (
    tampilkan_dasbor,
    tampilkan_form_transaksi,
    tampilkan_laporan,
    tampilkan_form_tabungan,
    tampilkan_riwayat_transaksi
)

# Inisialisasi latar belakang
tambah_latar_belakang("bg2.png")

# Judul Aplikasi
st.title("💰 Aplikasi Pengelolaan Keuangan")

# Tampilkan tanggal dan waktu saat ini
waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Tanggal dan Waktu Saat Ini: {waktu_sekarang}")

# Inisialisasi session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = []
if 'savings' not in st.session_state:
    st.session_state.savings = Tabungan()

# Sidebar untuk navigasi
st.sidebar.header("Navigasi")
halaman = st.sidebar.selectbox(
    "Pilih Halaman",
    ["🏠 Dasbor Utama", "📝 Pencatatan Transaksi", "📊 Pelaporan Keuangan", "💵 Menabung", "📝 Riwayat Transaksi"]
)

# Routing halaman
if halaman == "🏠 Dasbor Utama":
    tampilkan_dasbor(st.session_state.transactions, st.session_state.savings)
elif halaman == "📝 Pencatatan Transaksi":
    tampilkan_form_transaksi()
elif halaman == "📊 Pelaporan Keuangan":
    tampilkan_laporan()
elif halaman == "💵 Menabung":
    tampilkan_form_tabungan()
elif halaman == "📝 Riwayat Transaksi":
    tampilkan_riwayat_transaksi()