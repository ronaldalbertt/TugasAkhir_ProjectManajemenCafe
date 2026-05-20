from models.bahan_baku import BahanBaku
from models.produk_jadi import ProdukJadi
from models.peralatan_cafe import PeralatanCafe
from models.barang_kemasan import BarangKemasan


daftar_barang = [
    BahanBaku("BB001", "Biji Kopi Arabica", 10, 120000, "kg", "2026-12-30"),
    ProdukJadi("PJ001", "Cold Brew Bottle", 25, 12000, "Minuman Botol", 22000),
    PeralatanCafe("PC001", "Grinder Manual", 2, 350000, "Baik", 2025),
    BarangKemasan("BK001", "Paper Cup 12 oz", 100, 800, "12 oz", "Kertas"),
]

for barang in daftar_barang:
    print("=" * 50)
    print(barang.tampilkan_info())