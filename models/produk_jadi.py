from models.barang import Barang


class ProdukJadi(Barang):
    #Class untuk merepresentasikan produk siap jual, seperti cold brew bottle, dessert cup, dan roti kopi.


    def __init__(self, kode_barang, nama, stok, harga_beli, kategori_produk, harga_jual):
        super().__init__(kode_barang, nama, stok, harga_beli)
        self.__kategori_produk = self.validasi_teks(kategori_produk, "Kategori produk")
        self.__harga_jual = self.validasi_angka_positif(harga_jual, "Harga jual")

        if self.__harga_jual <= self.get_harga_beli():
            raise ValueError("Harga jual harus lebih besar dari harga beli.")

    # Getter
    def get_kategori_produk(self):
        return self.__kategori_produk

    def get_harga_jual(self):
        return self.__harga_jual

    # Setter dengan validasi
    def set_kategori_produk(self, kategori_baru):
        self.__kategori_produk = self.validasi_teks(kategori_baru, "Kategori produk")

    def set_harga_jual(self, harga_jual_baru):
        harga_jual_baru = self.validasi_angka_positif(harga_jual_baru, "Harga jual")

        if harga_jual_baru <= self.get_harga_beli():
            raise ValueError("Harga jual harus lebih besar dari harga beli.")

        self.__harga_jual = harga_jual_baru

    def hitung_potensi_keuntungan(self):
        keuntungan_per_item = self.__harga_jual - self.get_harga_beli()
        return keuntungan_per_item * self.get_stok()

    # Override method untuk polymorphism
    def tampilkan_info(self):
        return (
            f"{super().tampilkan_info()}\n"
            f"Jenis       : Produk Jadi\n"
            f"Kategori    : {self.__kategori_produk}\n"
            f"Harga Jual  : Rp{self.__harga_jual:,.0f}\n"
            f"Potensi Untung: Rp{self.hitung_potensi_keuntungan():,.0f}"
        )

    # Override method untuk JSON
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "jenis": "ProdukJadi",
            "kategori_produk": self.__kategori_produk,
            "harga_jual": self.__harga_jual
        })
        return data