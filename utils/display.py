import os


class DisplayHelper:
    """
    Helper class untuk mengatur tampilan CLI agar lebih rapi.
    """

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def tampilkan_header():
        print("╔══════════════════════════════════════════════╗")
        print("║        TIF CAFE INVENTORY SYSTEM            ║")
        print("║        Sistem Inventaris Cafe               ║")
        print("╚══════════════════════════════════════════════╝")

    @staticmethod
    def tampilkan_menu_utama():
        print("\n[1] Tambah Barang")
        print("[2] Tampilkan Semua Barang")
        print("[3] Cari Barang")
        print("[4] Ubah Data Barang")
        print("[5] Hapus Barang")
        print("[6] Laporan Stok")
        print("[7] Simpan Data")
        print("[0] Keluar")

    @staticmethod
    def tampilkan_menu_jenis_barang():
        print("\nPilih Jenis Barang:")
        print("[1] Bahan Baku")
        print("[2] Produk Jadi")
        print("[3] Peralatan Cafe")
        print("[4] Barang Kemasan")
        print("[0] Kembali")

    @staticmethod
    def tampilkan_menu_cari():
        print("\nCari berdasarkan:")
        print("[1] Kode Barang")
        print("[2] Nama Barang")
        print("[0] Kembali")

    @staticmethod
    def tampilkan_menu_laporan():
        print("\nMenu Laporan:")
        print("[1] Laporan Total Stok")
        print("[2] Laporan Nilai Inventaris")
        print("[3] Laporan Barang Stok Rendah")
        print("[4] Laporan Jumlah Jenis Barang")
        print("[0] Kembali")

    @staticmethod
    def tampilkan_garis():
        print("═" * 50)

    @staticmethod
    def tampilkan_pesan_sukses(pesan):
        print(f"\n[SUKSES] {pesan}")

    @staticmethod
    def tampilkan_pesan_error(pesan):
        print(f"\n[ERROR] {pesan}")

    @staticmethod
    def pause():
        input("\nTekan Enter untuk melanjutkan...")

    @staticmethod
    def tampilkan_detail_barang(barang):
        DisplayHelper.tampilkan_garis()
        print(barang.tampilkan_info())
        DisplayHelper.tampilkan_garis()

    @staticmethod
    def tampilkan_daftar_barang(daftar_barang):
        if len(daftar_barang) == 0:
            print("\nBelum ada data barang.")
            return

        for barang in daftar_barang:
            DisplayHelper.tampilkan_detail_barang(barang)