import json
import os

from models.bahan_baku import BahanBaku
from models.produk_jadi import ProdukJadi
from models.peralatan_cafe import PeralatanCafe
from models.barang_kemasan import BarangKemasan


class JsonStorage:
    # Class untuk mengatur penyimpanan dan pembacaan data barang   menggunakan file JSON.


    def __init__(self, file_path="data/barang.json"):
        self.__file_path = file_path

    def get_file_path(self):
        return self.__file_path

    def simpan_data(self, daftar_barang):
    #Menyimpan daftar objek barang ke file JSON.
        folder = os.path.dirname(self.__file_path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        data = []

        for barang in daftar_barang:
            data.append(barang.to_dict())

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def baca_data(self):
    #Membaca data dari file JSON lalu mengubahnya menjadi objek barang.

        if not os.path.exists(self.__file_path):
            return []

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            daftar_barang = []

            for item in data:
                barang = self.buat_objek_dari_dict(item)
                if barang is not None:
                    daftar_barang.append(barang)

            return daftar_barang

        except json.JSONDecodeError:
            return []

    def buat_objek_dari_dict(self, data):
    #Factory method sederhana untuk membuat objek berdasarkan jenis barang.
        jenis = data.get("jenis")

        if jenis == "BahanBaku":
            return BahanBaku(
                data.get("kode_barang"),
                data.get("nama"),
                data.get("stok"),
                data.get("harga_beli"),
                data.get("satuan"),
                data.get("tanggal_kedaluwarsa")
            )

        if jenis == "ProdukJadi":
            return ProdukJadi(
                data.get("kode_barang"),
                data.get("nama"),
                data.get("stok"),
                data.get("harga_beli"),
                data.get("kategori_produk"),
                data.get("harga_jual")
            )

        if jenis == "PeralatanCafe":
            return PeralatanCafe(
                data.get("kode_barang"),
                data.get("nama"),
                data.get("stok"),
                data.get("harga_beli"),
                data.get("kondisi"),
                data.get("tahun_pembelian")
            )

        if jenis == "BarangKemasan":
            return BarangKemasan(
                data.get("kode_barang"),
                data.get("nama"),
                data.get("stok"),
                data.get("harga_beli"),
                data.get("ukuran"),
                data.get("bahan_kemasan")
            )

        return None