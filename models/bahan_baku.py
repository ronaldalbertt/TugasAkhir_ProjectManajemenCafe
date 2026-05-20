from models.barang import Barang


class BahanBaku(Barang):
    #Class untuk merepresentasikan bahan baku cafe, seperti biji kopi, susu, gula aren, sirup, dan coklat bubuk.


    def __init__(self, kode_barang, nama, stok, harga_beli, satuan, tanggal_kedaluwarsa):
        super().__init__(kode_barang, nama, stok, harga_beli)
        self.__satuan = self.validasi_teks(satuan, "Satuan")
        self.__tanggal_kedaluwarsa = self.validasi_tanggal(tanggal_kedaluwarsa)

    # Getter
    def get_satuan(self):
        return self.__satuan

    def get_tanggal_kedaluwarsa(self):
        return self.__tanggal_kedaluwarsa

    # Setter dengan validasi
    def set_satuan(self, satuan_baru):
        self.__satuan = self.validasi_teks(satuan_baru, "Satuan")

    def set_tanggal_kedaluwarsa(self, tanggal_baru):
        self.__tanggal_kedaluwarsa = self.validasi_tanggal(tanggal_baru)

    def cek_kedaluwarsa(self):
        return f"Bahan baku {self.get_nama()} kedaluwarsa pada {self.__tanggal_kedaluwarsa}."

    # Override method untuk polymorphism
    def tampilkan_info(self):
        return (
            f"{super().tampilkan_info()}\n"
            f"Jenis       : Bahan Baku\n"
            f"Satuan      : {self.__satuan}\n"
            f"Expired     : {self.__tanggal_kedaluwarsa}"
        )

    # Override method untuk JSON
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "jenis": "BahanBaku",
            "satuan": self.__satuan,
            "tanggal_kedaluwarsa": self.__tanggal_kedaluwarsa
        })
        return data