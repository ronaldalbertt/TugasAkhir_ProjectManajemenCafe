from datetime import datetime


class ValidasiMixin:

    def validasi_teks(self, nilai, nama_field):
        if not isinstance(nilai, str) or nilai.strip() == "":
            raise ValueError(f"{nama_field} tidak boleh kosong.")
        return nilai.strip()

    def validasi_angka_positif(self, nilai, nama_field):
        try:
            nilai = float(nilai)
        except ValueError:
            raise ValueError(f"{nama_field} harus berupa angka.")

        if nilai <= 0:
            raise ValueError(f"{nama_field} harus lebih dari 0.")

        return nilai

    def validasi_stok(self, stok):
        try:
            stok = int(stok)
        except ValueError:
            raise ValueError("Stok harus berupa angka bulat.")

        if stok < 0:
            raise ValueError("Stok tidak boleh negatif.")

        return stok

    def validasi_tahun(self, tahun):
        try:
            tahun = int(tahun)
        except ValueError:
            raise ValueError("Tahun pembelian harus berupa angka.")

        if tahun < 1900 or tahun > 2100:
            raise ValueError("Tahun pembelian tidak valid.")

        return tahun

    def validasi_tanggal(self, tanggal):
        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format tanggal harus YYYY-MM-DD.")

        return tanggal