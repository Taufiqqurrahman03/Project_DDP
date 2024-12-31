# halaman.py
import streamlit as st
import pandas as pd
from datetime import datetime
from model_data import Transaksi

def tampilkan_dasbor(transaksi_list, tabungan):
    """Menampilkan halaman dasbor utama"""
    st.header("📊 Ringkasan Keuangan")
    from perhitungan_keuangan import hitung_keuangan
    total_pemasukan, total_pengeluaran, saldo = hitung_keuangan(transaksi_list)
    total_tabungan = tabungan.total_tabungan()
    
    st.metric(label="Total Pemasukan", value=f"{total_pemasukan} IDR")
    st.metric(label="Total Pengeluaran", value=f"{total_pengeluaran} IDR")
    st.metric(label="Saldo Saat Ini", value=f"{saldo} IDR")
    st.metric(label="Total Tabungan Anda", value=f"{total_tabungan} IDR")

def tampilkan_form_transaksi():
    """Menampilkan form pencatatan transaksi"""
    st.header("🖊️ Pencatatan Transaksi")

    tanggal = st.date_input("Tanggal")
    jenis = st.radio("Jenis Transaksi", ["Pemasukan", "Pengeluaran"])

    if jenis == "Pemasukan":
        kategori = st.selectbox("Pilih Sumber Dana", [
            "Orang Tua atau Keluarga", 
            "Beasiswa", 
            "Hasil Usaha", 
            "Hasil Kerja", 
            "Hibah", 
            "Tabungan Pribadi", 
            "Lainnya"
        ])
    else:
        kategori = st.selectbox("Pilih Kategori Pengeluaran", [
            "Makanan", 
            "Transportasi", 
            "Hiburan", 
            "Pendidikan", 
            "Lainnya"
        ])

    jumlah = st.number_input("Jumlah Uang", min_value=0.0, format="%.2f")
    catatan = st.text_input("Catatan Tambahan (opsional)")

    with st.form(key='form_transaksi'):
        tombol_submit = st.form_submit_button("Tambah Transaksi")
        if tombol_submit:
            transaksi = Transaksi(tanggal, jenis, kategori, jumlah, catatan, "transaksi")
            st.session_state.transactions.append(transaksi)
            st.success("Transaksi berhasil ditambahkan!")

def tampilkan_form_tabungan():
    """Menampilkan form tabungan"""
    st.header("💰 Menabung")
    with st.form(key='form_tabungan'):
        tanggal = st.date_input("Tanggal")
        tujuan = st.text_input("Menabung untuk apa?")
        jumlah = st.number_input("Jumlah Uang", min_value=0.0, format="%.2f")
        mata_uang = st.selectbox("Jenis Mata Uang", ["IDR", "USD", "EUR", "JPY"])
        
        tombol_submit = st.form_submit_button("Tambah Tabungan")
        if tombol_submit:
            # Tambahkan ke daftar tabungan
            st.session_state.savings.tambah_tabungan(tanggal, tujuan, jumlah, mata_uang)
            
            # Tambahkan juga ke daftar transaksi
            transaksi_tabungan = Transaksi(
                tanggal=tanggal,
                jenis="Pengeluaran",
                kategori="Tabungan",
                jumlah=jumlah,
                catatan=f"Tabungan untuk: {tujuan} ({mata_uang})",
                sumber="tabungan"
            )
            st.session_state.transactions.append(transaksi_tabungan)
            
            st.success("Tabungan berhasil ditambahkan!")

def tampilkan_riwayat_transaksi():
    """Menampilkan halaman riwayat transaksi"""
    st.header("📜 Riwayat Transaksi")
    
    # Filter untuk tipe transaksi
    tipe_filter = st.multiselect(
        "Filter berdasarkan tipe:",
        ["Transaksi", "Tabungan"],
        default=["Transaksi", "Tabungan"]
    )
    
    if st.session_state.transactions:
        # Filter transaksi berdasarkan pilihan
        transaksi_filtered = [
            t for t in st.session_state.transactions 
            if (t.sumber.capitalize() in tipe_filter)
        ]
        
        if transaksi_filtered:
            data = {
                "Tanggal": [t.tanggal for t in transaksi_filtered],
                "Jenis": [t.jenis for t in transaksi_filtered],
                "Kategori": [t.kategori for t in transaksi_filtered],
                "Jumlah (IDR)": [t.jumlah for t in transaksi_filtered],
                "Catatan": [t.catatan for t in transaksi_filtered],
                "Tipe": [t.sumber.capitalize() for t in transaksi_filtered]
            }
            
            df_transaksi = pd.DataFrame(data)
            # Urutkan berdasarkan tanggal, terbaru di atas
            df_transaksi = df_transaksi.sort_values(by='Tanggal', ascending=False)
            st.dataframe(df_transaksi, use_container_width=True)
        else:
            st.write("Tidak ada transaksi yang sesuai dengan filter.")
    else:
        st.write("Belum ada transaksi yang dicatat.")

def tampilkan_laporan():
    """Menampilkan halaman laporan keuangan"""
    st.header("📈 Pelaporan Keuangan")
    periode = st.selectbox("Pilih Periode Laporan", ["Harian", "Mingguan", "Bulanan", "Tahunan"])
    
    if st.button("Tampilkan Laporan"):
        from perhitungan_keuangan import buat_laporan
        total_pemasukan, total_pengeluaran, kategori_terbesar = buat_laporan(st.session_state.transactions, periode)
        
        if total_pemasukan is not None:
            st.subheader(f"Laporan {periode}")
            st.write(f"**Total Pemasukan:** {total_pemasukan} IDR")
            st.write(f"**Total Pengeluaran:** {total_pengeluaran} IDR")
            st.write(f"**Kategori Pengeluaran Terbesar:** {kategori_terbesar}")
        else:
            st.write("Tidak ada transaksi untuk periode ini.")