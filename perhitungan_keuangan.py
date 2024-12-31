
from datetime import datetime, timedelta

def hitung_keuangan(transaksi_list):
    """Menghitung total pemasukan, pengeluaran, dan saldo"""
    total_pemasukan = sum(t.jumlah for t in transaksi_list if t.jenis == 'Pemasukan')
    total_pengeluaran = sum(t.jumlah for t in transaksi_list if t.jenis == 'Pengeluaran')
    saldo = total_pemasukan - total_pengeluaran
    return total_pemasukan, total_pengeluaran, saldo

def buat_laporan(transaksi_list, periode):
    """Membuat laporan keuangan berdasarkan periode tertentu"""
    if not transaksi_list:
        return None, None, None

    hari_ini = datetime.today()
    if periode == "Harian":
        tanggal_mulai = hari_ini - timedelta(days=1)
    elif periode == "Mingguan":
        tanggal_mulai = hari_ini - timedelta(days=hari_ini.weekday() + 7)
    elif periode == "Bulanan":
        tanggal_mulai = hari_ini.replace(day=1) - timedelta(days=1)
    elif periode == "Tahunan":
        tanggal_mulai = hari_ini.replace(month=1, day=1) - timedelta(days=1)

    tanggal_mulai = tanggal_mulai.date()

    transaksi_terfilter = [t for t in transaksi_list if t.tanggal > tanggal_mulai]
    total_pemasukan = sum(t.jumlah for t in transaksi_terfilter if t.jenis == 'Pemasukan')
    total_pengeluaran = sum(t.jumlah for t in transaksi_terfilter if t.jenis == 'Pengeluaran')
    
    if transaksi_terfilter:
        kategori_terbesar = max(
            set(t.kategori for t in transaksi_terfilter if t.jenis == 'Pengeluaran'), 
            key=lambda x: sum(t.jumlah for t in transaksi_terfilter if t.jenis == 'Pengeluaran' and t.kategori == x), 
            default="Tidak ada"
        )
    else:
        kategori_terbesar = "Tidak ada"

    return total_pemasukan, total_pengeluaran, kategori_terbesar