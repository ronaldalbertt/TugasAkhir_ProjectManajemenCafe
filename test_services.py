from models.bahan_baku import BahanBaku
from models.produk_jadi import ProdukJadi
from models.peralatan_cafe import PeralatanCafe
from models.barang_kemasan import BarangKemasan

from services.manajemen_barang import ManajemenBarang
from services.laporan_stok import LaporanStok
from services.json_storage import JsonStorage


barang1 = BahanBaku("BB001", "Biji Kopi Arabica", 10, 120000, "kg", "2026-12-30")
barang2 = ProdukJadi("PJ001", "Cold Brew Bottle", 25, 12000, "Minuman Botol", 22000)
barang3 = PeralatanCafe("PC001", "Grinder Manual", 2, 350000, "Baik", 2025)
barang4 = BarangKemasan("BK001", "Paper Cup 12 oz", 100, 800, "12 oz", "Kertas")

manajemen = ManajemenBarang()

manajemen.tambah_barang(barang1)
manajemen.tambah_barang(barang2)
manajemen.tambah_barang(barang3)
manajemen.tambah_barang(barang4)

print("\n=== SEMUA BARANG ===")
for barang in manajemen.tampilkan_semua_barang():
    print("=" * 50)
    print(barang.tampilkan_info())

print("\n=== CARI BARANG BY KODE ===")
hasil = manajemen.cari_barang_by_kode("BB001")
print(hasil.tampilkan_info())

print("\n=== LAPORAN STOK ===")
laporan = LaporanStok(manajemen.get_daftar_barang())
print(f"Total Stok: {laporan.hitung_total_stok()}")
print(f"Total Nilai Inventaris: Rp{laporan.hitung_total_nilai_inventaris():,.0f}")

print("\n=== STOK RENDAH <= 5 ===")
stok_rendah = laporan.tampilkan_barang_stok_rendah(5)
for barang in stok_rendah:
    print(f"{barang.get_kode_barang()} - {barang.get_nama()} - Stok: {barang.get_stok()}")

print("\n=== SIMPAN KE JSON ===")
storage = JsonStorage()
storage.simpan_data(manajemen.get_daftar_barang())
print("Data berhasil disimpan.")

print("\n=== BACA DARI JSON ===")
data_dari_json = storage.baca_data()
for barang in data_dari_json:
    print(f"{barang.get_kode_barang()} - {barang.get_nama()} - {barang.__class__.__name__}")