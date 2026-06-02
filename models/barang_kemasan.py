from models.barang import Barang


class BarangKemasan(Barang):
    # Class untuk merepresentasikan barang kemasan cafe, seperti paper cup, sedotan, tutup gelas, dan paper bag.


    def __init__(self, kode_barang, nama, stok, harga_beli, ukuran, bahan_kemasan):
        kode_barang = self.validasi_kode_prefix(kode_barang, "BK", "Barang Kemasan")
        super().__init__(kode_barang, nama, stok, harga_beli)
        self.__ukuran = self.validasi_teks(ukuran, "Ukuran")
        self.__bahan_kemasan = self.validasi_teks(bahan_kemasan, "Bahan kemasan")

    # Getter
    def get_ukuran(self):
        return self.__ukuran

    def get_bahan_kemasan(self):
        return self.__bahan_kemasan

    # Setter dengan validasi
    def set_ukuran(self, ukuran_baru):
        self.__ukuran = self.validasi_teks(ukuran_baru, "Ukuran")

    def set_bahan_kemasan(self, bahan_baru):
        self.__bahan_kemasan = self.validasi_teks(bahan_baru, "Bahan kemasan")

    # Override method untuk polymorphism
    def tampilkan_info(self):
        return (
            f"{super().tampilkan_info()}\n"
            f"Jenis       : Barang Kemasan\n"
            f"Ukuran      : {self.__ukuran}\n"
            f"Bahan       : {self.__bahan_kemasan}"
        )

    # Override method untuk JSON
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "jenis": "BarangKemasan",
            "ukuran": self.__ukuran,
            "bahan_kemasan": self.__bahan_kemasan
        })
        return data