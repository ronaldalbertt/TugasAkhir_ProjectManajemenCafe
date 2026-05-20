from models.barang import Barang


class PeralatanCafe(Barang):
    #  Class untuk merepresentasikan peralatan cafe, seperti grinder, mesin espresso, timbangan digital, dan kettle.


    DAFTAR_KONDISI = ["Baik", "Rusak Ringan", "Rusak Berat"]

    def __init__(self, kode_barang, nama, stok, harga_beli, kondisi, tahun_pembelian):
        super().__init__(kode_barang, nama, stok, harga_beli)
        self.__kondisi = self.__validasi_kondisi(kondisi)
        self.__tahun_pembelian = self.validasi_tahun(tahun_pembelian)

    def __validasi_kondisi(self, kondisi):
        kondisi = self.validasi_teks(kondisi, "Kondisi")

        for pilihan in self.DAFTAR_KONDISI:
            if kondisi.lower() == pilihan.lower():
                return pilihan

        raise ValueError("Kondisi harus: Baik, Rusak Ringan, atau Rusak Berat.")

    # Getter
    def get_kondisi(self):
        return self.__kondisi

    def get_tahun_pembelian(self):
        return self.__tahun_pembelian

    # Setter dengan validasi
    def set_kondisi(self, kondisi_baru):
        self.__kondisi = self.__validasi_kondisi(kondisi_baru)

    def set_tahun_pembelian(self, tahun_baru):
        self.__tahun_pembelian = self.validasi_tahun(tahun_baru)

    def cek_status_peralatan(self):
        if self.__kondisi == "Baik":
            return f"Peralatan {self.get_nama()} masih layak digunakan."
        elif self.__kondisi == "Rusak Ringan":
            return f"Peralatan {self.get_nama()} perlu diperiksa."
        return f"Peralatan {self.get_nama()} harus segera diperbaiki atau diganti."

    # Override method untuk polymorphism
    def tampilkan_info(self):
        return (
            f"{super().tampilkan_info()}\n"
            f"Jenis       : Peralatan Cafe\n"
            f"Kondisi     : {self.__kondisi}\n"
            f"Tahun Beli  : {self.__tahun_pembelian}\n"
            f"Status      : {self.cek_status_peralatan()}"
        )

    # Override method untuk JSON
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "jenis": "PeralatanCafe",
            "kondisi": self.__kondisi,
            "tahun_pembelian": self.__tahun_pembelian
        })
        return data