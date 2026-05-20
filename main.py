from models.bahan_baku import BahanBaku
from models.produk_jadi import ProdukJadi
from models.peralatan_cafe import PeralatanCafe
from models.barang_kemasan import BarangKemasan

from services.json_storage import JsonStorage
from services.manajemen_barang import ManajemenBarang
from services.laporan_stok import LaporanStok

from utils.display import DisplayHelper


storage = JsonStorage()
manajemen = ManajemenBarang(storage.baca_data())


def input_data_umum():
    kode_barang = input("Kode Barang  : ")
    nama = input("Nama Barang  : ")
    stok = input("Stok         : ")
    harga_beli = input("Harga Beli   : ")

    return kode_barang, nama, stok, harga_beli


def tambah_barang():
    while True:
        DisplayHelper.clear_screen()
        DisplayHelper.tampilkan_header()
        DisplayHelper.tampilkan_menu_jenis_barang()

        pilihan = input("\nPilih jenis barang: ")

        if pilihan == "0":
            return

        try:
            if pilihan == "1":
                kode_barang, nama, stok, harga_beli = input_data_umum()
                satuan = input("Satuan              : ")
                tanggal = input("Tanggal Expired     : ")

                barang = BahanBaku(
                    kode_barang,
                    nama,
                    stok,
                    harga_beli,
                    satuan,
                    tanggal
                )

            elif pilihan == "2":
                kode_barang, nama, stok, harga_beli = input_data_umum()
                kategori = input("Kategori Produk     : ")
                harga_jual = input("Harga Jual          : ")

                barang = ProdukJadi(
                    kode_barang,
                    nama,
                    stok,
                    harga_beli,
                    kategori,
                    harga_jual
                )

            elif pilihan == "3":
                kode_barang, nama, stok, harga_beli = input_data_umum()
                kondisi = input("Kondisi             : ")
                tahun = input("Tahun Pembelian     : ")

                barang = PeralatanCafe(
                    kode_barang,
                    nama,
                    stok,
                    harga_beli,
                    kondisi,
                    tahun
                )

            elif pilihan == "4":
                kode_barang, nama, stok, harga_beli = input_data_umum()
                ukuran = input("Ukuran              : ")
                bahan = input("Bahan Kemasan       : ")

                barang = BarangKemasan(
                    kode_barang,
                    nama,
                    stok,
                    harga_beli,
                    ukuran,
                    bahan
                )

            else:
                DisplayHelper.tampilkan_pesan_error("Pilihan tidak valid.")
                DisplayHelper.pause()
                continue

            manajemen.tambah_barang(barang)
            storage.simpan_data(manajemen.get_daftar_barang())
            DisplayHelper.tampilkan_pesan_sukses("Barang berhasil ditambahkan dan disimpan.")
            DisplayHelper.pause()
            return

        except ValueError as error:
            DisplayHelper.tampilkan_pesan_error(error)
            DisplayHelper.pause()


def tampilkan_semua_barang():
    DisplayHelper.clear_screen()
    DisplayHelper.tampilkan_header()
    print("\nDAFTAR SEMUA BARANG")
    DisplayHelper.tampilkan_daftar_barang(manajemen.tampilkan_semua_barang())
    DisplayHelper.pause()


def cari_barang():
    while True:
        DisplayHelper.clear_screen()
        DisplayHelper.tampilkan_header()
        DisplayHelper.tampilkan_menu_cari()

        pilihan = input("\nPilih menu cari: ")

        if pilihan == "0":
            return

        if pilihan == "1":
            kode = input("Masukkan kode barang: ")
            barang = manajemen.cari_barang_by_kode(kode)

            if barang is None:
                DisplayHelper.tampilkan_pesan_error("Barang tidak ditemukan.")
            else:
                DisplayHelper.tampilkan_detail_barang(barang)

            DisplayHelper.pause()

        elif pilihan == "2":
            nama = input("Masukkan nama barang: ")
            hasil = manajemen.cari_barang_by_nama(nama)

            if len(hasil) == 0:
                DisplayHelper.tampilkan_pesan_error("Barang tidak ditemukan.")
            else:
                DisplayHelper.tampilkan_daftar_barang(hasil)

            DisplayHelper.pause()

        else:
            DisplayHelper.tampilkan_pesan_error("Pilihan tidak valid.")
            DisplayHelper.pause()


def ubah_atribut_khusus(barang):
    nama_class = barang.__class__.__name__

    print("\nPilih atribut khusus yang ingin diubah:")

    if nama_class == "BahanBaku":
        print("[1] Satuan")
        print("[2] Tanggal Kedaluwarsa")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            nilai = input("Satuan baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "satuan", nilai)
        elif pilihan == "2":
            nilai = input("Tanggal kedaluwarsa baru YYYY-MM-DD: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "tanggal_kedaluwarsa", nilai)
        else:
            raise ValueError("Pilihan atribut tidak valid.")

    elif nama_class == "ProdukJadi":
        print("[1] Kategori Produk")
        print("[2] Harga Jual")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            nilai = input("Kategori produk baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "kategori_produk", nilai)
        elif pilihan == "2":
            nilai = input("Harga jual baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "harga_jual", nilai)
        else:
            raise ValueError("Pilihan atribut tidak valid.")

    elif nama_class == "PeralatanCafe":
        print("[1] Kondisi")
        print("[2] Tahun Pembelian")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            nilai = input("Kondisi baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "kondisi", nilai)
        elif pilihan == "2":
            nilai = input("Tahun pembelian baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "tahun_pembelian", nilai)
        else:
            raise ValueError("Pilihan atribut tidak valid.")

    elif nama_class == "BarangKemasan":
        print("[1] Ukuran")
        print("[2] Bahan Kemasan")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            nilai = input("Ukuran baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "ukuran", nilai)
        elif pilihan == "2":
            nilai = input("Bahan kemasan baru: ")
            manajemen.ubah_atribut_khusus(barang.get_kode_barang(), "bahan_kemasan", nilai)
        else:
            raise ValueError("Pilihan atribut tidak valid.")

    else:
        raise ValueError("Jenis barang tidak dikenali.")


def ubah_data_barang():
    DisplayHelper.clear_screen()
    DisplayHelper.tampilkan_header()

    kode = input("Masukkan kode barang yang ingin diubah: ")
    barang = manajemen.cari_barang_by_kode(kode)

    if barang is None:
        DisplayHelper.tampilkan_pesan_error("Barang tidak ditemukan.")
        DisplayHelper.pause()
        return

    DisplayHelper.tampilkan_detail_barang(barang)

    print("\nPilih data yang ingin diubah:")
    print("[1] Nama")
    print("[2] Stok")
    print("[3] Harga Beli")
    print("[4] Atribut Khusus")
    print("[0] Kembali")

    pilihan = input("Pilih: ")

    try:
        if pilihan == "1":
            nama_baru = input("Nama baru: ")
            manajemen.ubah_nama_barang(kode, nama_baru)

        elif pilihan == "2":
            stok_baru = input("Stok baru: ")
            manajemen.ubah_stok_barang(kode, stok_baru)

        elif pilihan == "3":
            harga_baru = input("Harga beli baru: ")
            manajemen.ubah_harga_beli_barang(kode, harga_baru)

        elif pilihan == "4":
            ubah_atribut_khusus(barang)

        elif pilihan == "0":
            return

        else:
            DisplayHelper.tampilkan_pesan_error("Pilihan tidak valid.")
            DisplayHelper.pause()
            return

        storage.simpan_data(manajemen.get_daftar_barang())
        DisplayHelper.tampilkan_pesan_sukses("Data barang berhasil diubah dan disimpan.")
        DisplayHelper.pause()

    except ValueError as error:
        DisplayHelper.tampilkan_pesan_error(error)
        DisplayHelper.pause()


def hapus_barang():
    DisplayHelper.clear_screen()
    DisplayHelper.tampilkan_header()

    kode = input("Masukkan kode barang yang ingin dihapus: ")

    try:
        manajemen.hapus_barang(kode)
        storage.simpan_data(manajemen.get_daftar_barang())
        DisplayHelper.tampilkan_pesan_sukses("Barang berhasil dihapus dan data disimpan.")
    except ValueError as error:
        DisplayHelper.tampilkan_pesan_error(error)

    DisplayHelper.pause()


def laporan_stok():
    while True:
        DisplayHelper.clear_screen()
        DisplayHelper.tampilkan_header()
        DisplayHelper.tampilkan_menu_laporan()

        laporan = LaporanStok(manajemen.get_daftar_barang())
        pilihan = input("\nPilih menu laporan: ")

        if pilihan == "0":
            return

        elif pilihan == "1":
            total_stok = laporan.hitung_total_stok()
            print(f"\nTotal seluruh stok barang: {total_stok}")

        elif pilihan == "2":
            total_nilai = laporan.hitung_total_nilai_inventaris()
            print(f"\nTotal nilai inventaris: Rp{total_nilai:,.0f}")

        elif pilihan == "3":
            try:
                batas = input("Masukkan batas stok rendah: ")
                hasil = laporan.tampilkan_barang_stok_rendah(batas)

                print(f"\nBarang dengan stok <= {batas}:")
                DisplayHelper.tampilkan_daftar_barang(hasil)

            except ValueError as error:
                DisplayHelper.tampilkan_pesan_error(error)

        elif pilihan == "4":
            hasil = laporan.hitung_jumlah_jenis_barang()

            if len(hasil) == 0:
                print("\nBelum ada data barang.")
            else:
                print("\nJumlah barang berdasarkan jenis:")
                for jenis, jumlah in hasil.items():
                    print(f"- {jenis}: {jumlah} barang")

        else:
            DisplayHelper.tampilkan_pesan_error("Pilihan tidak valid.")

        DisplayHelper.pause()


def simpan_data():
    storage.simpan_data(manajemen.get_daftar_barang())
    DisplayHelper.tampilkan_pesan_sukses("Data berhasil disimpan.")
    DisplayHelper.pause()


def main():
    while True:
        DisplayHelper.clear_screen()
        DisplayHelper.tampilkan_header()
        DisplayHelper.tampilkan_menu_utama()

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tambah_barang()

        elif pilihan == "2":
            tampilkan_semua_barang()

        elif pilihan == "3":
            cari_barang()

        elif pilihan == "4":
            ubah_data_barang()

        elif pilihan == "5":
            hapus_barang()

        elif pilihan == "6":
            laporan_stok()

        elif pilihan == "7":
            simpan_data()

        elif pilihan == "0":
            storage.simpan_data(manajemen.get_daftar_barang())
            print("\nTerima kasih telah menggunakan TIF Cafe Inventory System.")
            break

        else:
            DisplayHelper.tampilkan_pesan_error("Pilihan tidak valid.")
            DisplayHelper.pause()


if __name__ == "__main__":
    main()