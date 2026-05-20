from interfaces.item_interface import ItemInterface
from mixins.validasi_mixin import ValidasiMixin


class Barang(ItemInterface, ValidasiMixin):

    def __init__(self, kode_barang, nama, stok, harga_beli):
        self.__kode_barang = self.validasi_teks(kode_barang, "Kode barang")
        self.__nama = self.validasi_teks(nama, "Nama barang")
        self.__stok = self.validasi_stok(stok)
        self.__harga_beli = self.validasi_angka_positif(harga_beli, "Harga beli")

    # Getter
    def get_kode_barang(self):
        return self.__kode_barang

    def get_nama(self):
        return self.__nama

    def get_stok(self):
        return self.__stok

    def get_harga_beli(self):
        return self.__harga_beli

    # Setter dengan validasi
    def set_nama(self, nama_baru):
        self.__nama = self.validasi_teks(nama_baru, "Nama barang")

    def set_stok(self, stok_baru):
        self.__stok = self.validasi_stok(stok_baru)

    def set_harga_beli(self, harga_beli_baru):
        self.__harga_beli = self.validasi_angka_positif(
            harga_beli_baru,
            "Harga beli"
        )

    # Method manipulasi stok
    def tambah_stok(self, jumlah):
        jumlah = self.validasi_stok(jumlah)
        if jumlah <= 0:
            raise ValueError("Jumlah penambahan stok harus lebih dari 0.")

        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        jumlah = self.validasi_stok(jumlah)
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0.")

        if jumlah > self.__stok:
            raise ValueError("Jumlah pengurangan melebihi stok tersedia.")

        self.__stok -= jumlah

    # Implementasi method dari ItemInterface
    def hitung_nilai_stok(self):
        return self.__stok * self.__harga_beli

    def tampilkan_info(self):
        return (
            f"Kode Barang : {self.__kode_barang}\n"
            f"Nama Barang : {self.__nama}\n"
            f"Stok        : {self.__stok}\n"
            f"Harga Beli  : Rp{self.__harga_beli:,.0f}\n"
            f"Nilai Stok  : Rp{self.hitung_nilai_stok():,.0f}"
        )

    def to_dict(self):
        return {
            "jenis": "Barang",
            "kode_barang": self.__kode_barang,
            "nama": self.__nama,
            "stok": self.__stok,
            "harga_beli": self.__harga_beli
        }