class LaporanStok:
    #Class service untuk membuat laporan stok barang.

    def __init__(self, daftar_barang):
        self.__daftar_barang = daftar_barang

    def get_daftar_barang(self):
        return self.__daftar_barang

    def hitung_total_stok(self):
        total = 0

        for barang in self.__daftar_barang:
            total += barang.get_stok()

        return total

    def hitung_total_nilai_inventaris(self):
        total = 0

        for barang in self.__daftar_barang:
            total += barang.hitung_nilai_stok()

        return total

    def tampilkan_barang_stok_rendah(self, batas_stok):
        try:
            batas_stok = int(batas_stok)
        except ValueError:
            raise ValueError("Batas stok harus berupa angka bulat.")

        if batas_stok < 0:
            raise ValueError("Batas stok tidak boleh negatif.")

        hasil = []

        for barang in self.__daftar_barang:
            if barang.get_stok() <= batas_stok:
                hasil.append(barang)

        return hasil

    def hitung_jumlah_jenis_barang(self):
    #Menghitung jumlah barang berdasarkan jenis class.Ini opsional, tapi bagus untuk laporan tambahan.
        hasil = {}

        for barang in self.__daftar_barang:
            jenis = barang.__class__.__name__

            if jenis not in hasil:
                hasil[jenis] = 0

            hasil[jenis] += 1

        return hasil