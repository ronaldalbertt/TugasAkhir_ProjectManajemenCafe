from mixins.loggable_mixin import LoggableMixin


class ManajemenBarang(LoggableMixin):
    #Class service untuk mengelola kumpulan objek barang.Berisi operasi tambah, hapus, ubah, cari, dan tampilkan barang.

    def __init__(self, daftar_barang=None):
        if daftar_barang is None:
            self.__daftar_barang = []
        else:
            self.__daftar_barang = daftar_barang

    def get_daftar_barang(self):
        return self.__daftar_barang

    def set_daftar_barang(self, daftar_barang):
        if not isinstance(daftar_barang, list):
            raise ValueError("Daftar barang harus berupa list.")
        self.__daftar_barang = daftar_barang

    def tambah_barang(self, barang):
    #Menambahkan barang baru ke daftar barang.Kode barang wajib unik.
        if self.cari_barang_by_kode(barang.get_kode_barang()) is not None:
            raise ValueError("Kode barang sudah digunakan.")

        self.__daftar_barang.append(barang)
        self.buat_log(f"Barang {barang.get_kode_barang()} - {barang.get_nama()} berhasil ditambahkan.")

    def hapus_barang(self, kode_barang):
    #Menghapus barang berdasarkan kode barang.
        barang = self.cari_barang_by_kode(kode_barang)

        if barang is None:
            raise ValueError("Barang dengan kode tersebut tidak ditemukan.")

        self.__daftar_barang.remove(barang)
        self.buat_log(f"Barang {kode_barang} berhasil dihapus.")

    def cari_barang_by_kode(self, kode_barang):
    #Mencari barang berdasarkan kode barang.
        for barang in self.__daftar_barang:
            if barang.get_kode_barang().lower() == kode_barang.lower():
                return barang

        return None

    def cari_barang_by_nama(self, nama):
    #Mencari barang berdasarkan nama.Hasil bisa lebih dari satu karena nama bisa mirip.
        hasil = []

        for barang in self.__daftar_barang:
            if nama.lower() in barang.get_nama().lower():
                hasil.append(barang)

        return hasil

    def tampilkan_semua_barang(self):
    #Mengembalikan semua barang.
        return self.__daftar_barang

    def ubah_nama_barang(self, kode_barang, nama_baru):
        barang = self.cari_barang_by_kode(kode_barang)

        if barang is None:
            raise ValueError("Barang dengan kode tersebut tidak ditemukan.")

        barang.set_nama(nama_baru)
        self.buat_log(f"Nama barang {kode_barang} berhasil diubah.")

    def ubah_stok_barang(self, kode_barang, stok_baru):
        barang = self.cari_barang_by_kode(kode_barang)

        if barang is None:
            raise ValueError("Barang dengan kode tersebut tidak ditemukan.")

        barang.set_stok(stok_baru)
        self.buat_log(f"Stok barang {kode_barang} berhasil diubah.")

    def ubah_harga_beli_barang(self, kode_barang, harga_beli_baru):
        barang = self.cari_barang_by_kode(kode_barang)

        if barang is None:
            raise ValueError("Barang dengan kode tersebut tidak ditemukan.")

        barang.set_harga_beli(harga_beli_baru)
        self.buat_log(f"Harga beli barang {kode_barang} berhasil diubah.")

    def ubah_atribut_khusus(self, kode_barang, nama_atribut, nilai_baru):
    #Mengubah atribut khusus berdasarkan jenis barang.Method ini memakai pengecekan ketersediaan setter.
        barang = self.cari_barang_by_kode(kode_barang)

        if barang is None:
            raise ValueError("Barang dengan kode tersebut tidak ditemukan.")

        nama_method = f"set_{nama_atribut}"

        if not hasattr(barang, nama_method):
            raise ValueError("Atribut khusus tidak tersedia untuk jenis barang ini.")

        method_setter = getattr(barang, nama_method)
        method_setter(nilai_baru)

        self.buat_log(f"Atribut {nama_atribut} pada barang {kode_barang} berhasil diubah.")