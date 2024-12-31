# model_data.py
class Transaksi:
    """Kelas untuk menyimpan data transaksi"""
    def __init__(self, tanggal, jenis, kategori, jumlah, catatan, sumber="transaksi"):
        self.tanggal = tanggal
        self.jenis = jenis
        self.kategori = kategori
        self.jumlah = jumlah
        self.catatan = catatan
        self.sumber = sumber  # Menandakan apakah ini transaksi biasa atau dari tabungan

class Tabungan:
    """Kelas untuk mengelola data tabungan"""
    def __init__(self):
        self.daftar_tabungan = []

    def tambah_tabungan(self, tanggal, tujuan, jumlah, mata_uang):
        tabungan = {
            'Tanggal': tanggal,
            'Tujuan': tujuan,
            'Jumlah': jumlah,
            'Mata Uang': mata_uang
        }
        self.daftar_tabungan.append(tabungan)

    def total_tabungan(self):
        return sum(t['Jumlah'] for t in self.daftar_tabungan)