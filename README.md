# TIF Cafe Inventory System

**TIF Cafe Inventory System** adalah aplikasi berbasis **Command Line Interface (CLI)** yang digunakan untuk mengelola inventaris barang pada cafe atau toko kopi. Aplikasi ini dirancang untuk membantu proses pencatatan, pencarian, pengubahan, penghapusan, dan pelaporan stok barang cafe.

Project ini dibuat sebagai tugas akhir mata kuliah **Proyek Akhir 1 - Membangun Aplikasi** dengan menerapkan konsep **Object-Oriented Programming (OOP)**, yaitu:

- Enkapsulasi
- Abstraksi
- Abstract Base Class (ABC)
- Mixins
- Inheritance
- Polymorphism
- Modularitas kode
- Penyimpanan data menggunakan JSON

---

## 1. Deskripsi Aplikasi

TIF Cafe Inventory System berfokus pada pengelolaan data barang di lingkungan cafe. Barang yang dikelola tidak hanya berupa bahan baku, tetapi juga produk jadi, peralatan cafe, dan barang kemasan.

Aplikasi ini tidak dibuat sebagai sistem kasir atau transaksi penjualan, melainkan sebagai sistem inventaris yang berfokus pada pengelolaan data barang.

---

## 2. Tujuan Aplikasi

Tujuan dari aplikasi ini adalah:

1. Membantu pengelolaan data barang cafe secara sederhana dan terstruktur.
2. Menyediakan fitur tambah, ubah, hapus, cari, dan tampilkan data barang.
3. Menyediakan laporan stok dan nilai inventaris.
4. Menerapkan konsep OOP dalam pengembangan aplikasi Python.
5. Menunjukkan penggunaan class, object, inheritance, polymorphism, ABC, mixins, dan modularitas kode.
6. Menyimpan data secara permanen menggunakan file JSON.

---

## 3. Fitur Aplikasi

Fitur utama yang tersedia pada aplikasi ini adalah:

1. Tambah barang berdasarkan jenis barang.
2. Tampilkan semua data barang.
3. Cari barang berdasarkan kode barang.
4. Cari barang berdasarkan nama barang.
5. Ubah data barang.
6. Ubah atribut khusus sesuai jenis barang.
7. Hapus barang.
8. Laporan total stok.
9. Laporan total nilai inventaris.
10. Laporan barang dengan stok rendah.
11. Laporan jumlah barang berdasarkan jenis.
12. Simpan data ke file JSON.
13. Baca data dari file JSON saat aplikasi dijalankan.
14. Validasi input agar data tetap konsisten.

---

## 4. Jenis Barang

Aplikasi ini mengelola 4 jenis barang utama.

### 4.1 BahanBaku

Digunakan untuk merepresentasikan bahan baku cafe.

Contoh:

- Biji Kopi Arabica
- Susu UHT
- Gula Aren
- Sirup Vanilla
- Coklat Bubuk

Atribut khusus:

- Satuan
- Tanggal kedaluwarsa

Kode barang untuk BahanBaku diawali dengan:

```text
BB
```

Contoh:

```text
BB001
```

---

### 4.2 ProdukJadi

Digunakan untuk merepresentasikan produk siap jual.

Contoh:

- Cold Brew Bottle
- Roti Kopi
- Dessert Cup
- Minuman Botol

Atribut khusus:

- Kategori produk
- Harga jual

Kode barang untuk ProdukJadi diawali dengan:

```text
PJ
```

Contoh:

```text
PJ001
```

---

### 4.3 PeralatanCafe

Digunakan untuk merepresentasikan alat atau perlengkapan operasional cafe.

Contoh:

- Grinder Manual
- Mesin Espresso
- Milk Frother
- Timbangan Digital
- Kettle

Atribut khusus:

- Kondisi
- Tahun pembelian

Kode barang untuk PeralatanCafe diawali dengan:

```text
PC
```

Contoh:

```text
PC001
```

---

### 4.4 BarangKemasan

Digunakan untuk merepresentasikan barang kemasan yang digunakan cafe.

Contoh:

- Paper Cup
- Sedotan
- Tutup Gelas
- Paper Bag
- Cup Plastik

Atribut khusus:

- Ukuran
- Bahan kemasan

Kode barang untuk BarangKemasan diawali dengan:

```text
BK
```

Contoh:

```text
BK001
```

---

## 5. Aturan Validasi Data

Aplikasi ini menerapkan validasi input agar data yang disimpan tetap konsisten.

Aturan validasi yang digunakan:

1. Kode barang tidak boleh kosong.
2. Kode barang harus unik.
3. Kode barang harus sesuai dengan jenis barang:
    - `BB` untuk BahanBaku
    - `PJ` untuk ProdukJadi
    - `PC` untuk PeralatanCafe
    - `BK` untuk BarangKemasan

4. Nama barang tidak boleh kosong.
5. Stok harus berupa angka bulat.
6. Stok tidak boleh bernilai negatif.
7. Harga beli harus berupa angka.
8. Harga beli harus lebih dari 0.
9. Harga jual pada ProdukJadi harus lebih besar dari harga beli.
10. Tanggal kedaluwarsa harus menggunakan format `YYYY-MM-DD`.
11. Tahun pembelian harus berupa angka.
12. Kondisi peralatan hanya boleh berisi:
    - Baik
    - Rusak Ringan
    - Rusak Berat

Validasi ini bertujuan untuk menjaga konsistensi dan keamanan data.

---

## 6. Struktur Folder Project

Struktur folder aplikasi dibuat secara modular agar kode lebih mudah dipahami, digunakan kembali, dan dikembangkan.

```text
tif_cafe_inventory/
│
├── main.py
│
├── data/
│   └── barang.json
│
├── interfaces/
│   ├── __init__.py
│   └── item_interface.py
│
├── mixins/
│   ├── __init__.py
│   ├── validasi_mixin.py
│   └── loggable_mixin.py
│
├── models/
│   ├── __init__.py
│   ├── barang.py
│   ├── bahan_baku.py
│   ├── produk_jadi.py
│   ├── peralatan_cafe.py
│   └── barang_kemasan.py
│
├── services/
│   ├── __init__.py
│   ├── json_storage.py
│   ├── manajemen_barang.py
│   └── laporan_stok.py
│
├── utils/
│   ├── __init__.py
│   └── display.py
│
└── README.md
```

---

## 7. Penjelasan Folder dan File

### 7.1 `main.py`

File utama untuk menjalankan aplikasi. File ini berisi alur menu CLI dan menghubungkan fitur-fitur aplikasi.

File ini tidak menyimpan seluruh logic program agar kode tetap modular.

---

### 7.2 `data/barang.json`

File untuk menyimpan data barang secara permanen.

Data barang akan tetap tersedia walaupun aplikasi ditutup, karena data disimpan dalam format JSON.

---

### 7.3 `interfaces/item_interface.py`

Berisi class `ItemInterface` sebagai **Abstract Base Class (ABC)**.

Class ini mendefinisikan method wajib yang harus dimiliki oleh setiap class barang:

- `tampilkan_info()`
- `hitung_nilai_stok()`
- `to_dict()`

---

### 7.4 `mixins/validasi_mixin.py`

Berisi class `ValidasiMixin`.

Mixin ini menyediakan method validasi data, seperti:

- Validasi teks
- Validasi angka positif
- Validasi stok
- Validasi tanggal
- Validasi tahun
- Validasi prefix kode barang

---

### 7.5 `mixins/loggable_mixin.py`

Berisi class `LoggableMixin`.

Mixin ini digunakan untuk menampilkan log aktivitas, seperti ketika barang berhasil ditambahkan, diubah, atau dihapus.

---

### 7.6 `models/barang.py`

Berisi class `Barang` sebagai superclass utama.

Class ini menyimpan atribut umum semua barang, yaitu:

- Kode barang
- Nama barang
- Stok
- Harga beli

---

### 7.7 `models/bahan_baku.py`

Berisi class `BahanBaku`, yaitu subclass dari `Barang`.

Class ini digunakan untuk barang berupa bahan baku cafe.

---

### 7.8 `models/produk_jadi.py`

Berisi class `ProdukJadi`, yaitu subclass dari `Barang`.

Class ini digunakan untuk barang berupa produk siap jual.

---

### 7.9 `models/peralatan_cafe.py`

Berisi class `PeralatanCafe`, yaitu subclass dari `Barang`.

Class ini digunakan untuk barang berupa alat operasional cafe.

---

### 7.10 `models/barang_kemasan.py`

Berisi class `BarangKemasan`, yaitu subclass dari `Barang`.

Class ini digunakan untuk barang berupa kemasan cafe.

---

### 7.11 `services/json_storage.py`

Berisi class `JsonStorage`.

Class ini bertugas untuk:

- Menyimpan data barang ke file JSON
- Membaca data barang dari file JSON
- Mengubah data dictionary dari JSON menjadi objek barang

---

### 7.12 `services/manajemen_barang.py`

Berisi class `ManajemenBarang`.

Class ini bertugas mengelola data barang, seperti:

- Menambah barang
- Menghapus barang
- Mengubah data barang
- Mencari barang berdasarkan kode
- Mencari barang berdasarkan nama
- Menampilkan semua barang

---

### 7.13 `services/laporan_stok.py`

Berisi class `LaporanStok`.

Class ini bertugas menghasilkan laporan, seperti:

- Total stok
- Total nilai inventaris
- Barang dengan stok rendah
- Jumlah barang berdasarkan jenis

---

### 7.14 `utils/display.py`

Berisi class `DisplayHelper`.

Class ini digunakan untuk mengatur tampilan CLI agar lebih rapi dan mudah digunakan.

---

## 8. Konsep OOP yang Digunakan

### 8.1 Enkapsulasi

Enkapsulasi diterapkan dengan membuat atribut penting sebagai atribut private.

Contoh atribut private pada class `Barang`:

```python
self.__kode_barang
self.__nama
self.__stok
self.__harga_beli
```

Atribut tersebut tidak diubah secara langsung dari luar class. Perubahan data dilakukan melalui method setter, seperti:

```python
set_nama()
set_stok()
set_harga_beli()
```

Selain itu, setter dilengkapi validasi sehingga data yang masuk tetap aman dan konsisten.

Contoh aturan:

- Stok tidak boleh negatif.
- Harga beli harus lebih dari 0.
- Nama barang tidak boleh kosong.

---

### 8.2 Abstraksi

Abstraksi diterapkan menggunakan `ItemInterface` sebagai Abstract Base Class.

Class ini mendefinisikan antarmuka yang wajib diikuti oleh class barang.

Method abstract yang digunakan:

```python
tampilkan_info()
hitung_nilai_stok()
to_dict()
```

Dengan adanya ABC, setiap class barang wajib memiliki method tersebut. Hal ini membuat struktur class lebih konsisten.

---

### 8.3 Mixins

Aplikasi menggunakan mixins untuk menyediakan fungsionalitas tambahan tanpa mengubah hierarki class utama.

Mixin yang digunakan:

1. `ValidasiMixin`
2. `LoggableMixin`

`ValidasiMixin` digunakan untuk validasi data.

Contoh method:

```python
validasi_teks()
validasi_stok()
validasi_tanggal()
validasi_kode_prefix()
```

`LoggableMixin` digunakan untuk mencatat aktivitas aplikasi.

Contoh method:

```python
buat_log()
```

---

### 8.4 Inheritance

Inheritance diterapkan dengan menjadikan `Barang` sebagai superclass.

Subclass yang mewarisi `Barang` adalah:

```text
BahanBaku
ProdukJadi
PeralatanCafe
BarangKemasan
```

Relasi inheritance:

```text
Barang
├── BahanBaku
├── ProdukJadi
├── PeralatanCafe
└── BarangKemasan
```

Dengan inheritance, atribut umum seperti kode barang, nama, stok, dan harga beli cukup didefinisikan pada class `Barang`.

Subclass hanya menambahkan atribut khusus sesuai jenis barang.

---

### 8.5 Polymorphism

Polymorphism diterapkan melalui method yang sama, tetapi memiliki implementasi berbeda pada setiap subclass.

Contoh method:

```python
tampilkan_info()
to_dict()
```

Setiap subclass memiliki method `tampilkan_info()` sendiri.

Contoh:

- `BahanBaku.tampilkan_info()` menampilkan satuan dan tanggal kedaluwarsa.
- `ProdukJadi.tampilkan_info()` menampilkan kategori produk dan harga jual.
- `PeralatanCafe.tampilkan_info()` menampilkan kondisi dan tahun pembelian.
- `BarangKemasan.tampilkan_info()` menampilkan ukuran dan bahan kemasan.

Contoh penggunaan polymorphism:

```python
for barang in daftar_barang:
    print(barang.tampilkan_info())
```

Walaupun method yang dipanggil sama, output yang dihasilkan berbeda sesuai jenis objek.

---

### 8.6 Modularitas

Kode dipisahkan ke dalam beberapa folder berdasarkan tanggung jawab masing-masing.

Pembagian modul:

- `interfaces` untuk abstract class
- `mixins` untuk fungsi tambahan reusable
- `models` untuk class barang
- `services` untuk logic aplikasi
- `utils` untuk tampilan CLI
- `data` untuk penyimpanan JSON

Dengan modularitas ini, kode lebih mudah dibaca, diuji, dan dikembangkan.

---

## 9. Alur Penggunaan Aplikasi

Saat aplikasi dijalankan, user akan melihat menu utama:

```text
[1] Tambah Barang
[2] Tampilkan Semua Barang
[3] Cari Barang
[4] Ubah Data Barang
[5] Hapus Barang
[6] Laporan Stok
[7] Simpan Data
[0] Keluar
```

### 9.1 Tambah Barang

User memilih jenis barang yang ingin ditambahkan:

```text
[1] Bahan Baku
[2] Produk Jadi
[3] Peralatan Cafe
[4] Barang Kemasan
[0] Kembali
```

Setelah itu user mengisi data barang sesuai jenis barang.

---

### 9.2 Tampilkan Semua Barang

Aplikasi menampilkan seluruh data barang dalam bentuk tabel ringkas.

---

### 9.3 Cari Barang

User dapat mencari barang berdasarkan:

1. Kode barang
2. Nama barang

---

### 9.4 Ubah Data Barang

User memasukkan kode barang, lalu memilih data yang ingin diubah:

1. Nama
2. Stok
3. Harga beli
4. Atribut khusus

Atribut khusus akan menyesuaikan jenis barang.

---

### 9.5 Hapus Barang

User memasukkan kode barang yang ingin dihapus.

Sebelum data dihapus, aplikasi akan menampilkan detail barang dan meminta konfirmasi.

---

### 9.6 Laporan Stok

Aplikasi menyediakan beberapa laporan:

1. Total stok seluruh barang
2. Total nilai inventaris
3. Barang dengan stok rendah
4. Jumlah barang berdasarkan jenis

---

## 10. Penyimpanan Data JSON

Aplikasi menggunakan file JSON untuk menyimpan data barang.

Contoh data JSON:

```json
{
    "jenis": "BahanBaku",
    "kode_barang": "BB001",
    "nama": "Biji Kopi Arabica",
    "stok": 10,
    "harga_beli": 120000,
    "satuan": "kg",
    "tanggal_kedaluwarsa": "2026-12-30"
}
```

Field `jenis` digunakan agar program dapat mengetahui class mana yang harus dibuat saat data dibaca kembali dari JSON.

Contoh:

```text
jenis = BahanBaku       → objek BahanBaku
jenis = ProdukJadi      → objek ProdukJadi
jenis = PeralatanCafe   → objek PeralatanCafe
jenis = BarangKemasan   → objek BarangKemasan
```

---

## 11. Cara Menjalankan Aplikasi

Pastikan Python sudah terpasang.

Masuk ke folder project:

```bash
cd tif_cafe_inventory
```

Jalankan aplikasi:

```bash
python main.py
```

Jika menggunakan sistem tertentu yang memakai `python3`, jalankan:

```bash
python3 main.py
```

---

## 12. Contoh Data Awal

File `data/barang.json` dapat diisi dengan data awal berikut:

```json
[
    {
        "jenis": "BahanBaku",
        "kode_barang": "BB001",
        "nama": "Biji Kopi Arabica",
        "stok": 10,
        "harga_beli": 120000,
        "satuan": "kg",
        "tanggal_kedaluwarsa": "2026-12-30"
    },
    {
        "jenis": "BahanBaku",
        "kode_barang": "BB002",
        "nama": "Susu UHT",
        "stok": 5,
        "harga_beli": 18000,
        "satuan": "liter",
        "tanggal_kedaluwarsa": "2026-08-15"
    },
    {
        "jenis": "ProdukJadi",
        "kode_barang": "PJ001",
        "nama": "Cold Brew Bottle",
        "stok": 25,
        "harga_beli": 12000,
        "kategori_produk": "Minuman Botol",
        "harga_jual": 22000
    },
    {
        "jenis": "PeralatanCafe",
        "kode_barang": "PC001",
        "nama": "Grinder Manual",
        "stok": 2,
        "harga_beli": 350000,
        "kondisi": "Baik",
        "tahun_pembelian": 2025
    },
    {
        "jenis": "BarangKemasan",
        "kode_barang": "BK001",
        "nama": "Paper Cup 12 oz",
        "stok": 100,
        "harga_beli": 800,
        "ukuran": "12 oz",
        "bahan_kemasan": "Kertas"
    }
]
```

---

## 13. Checklist Pengujian

Pengujian dilakukan untuk memastikan aplikasi berjalan dengan baik dan validasi data bekerja dengan benar.

| No  | Pengujian                                                       | Hasil yang Diharapkan            |
| --- | --------------------------------------------------------------- | -------------------------------- |
| 1   | Tambah BahanBaku dengan kode `BB003`                            | Berhasil                         |
| 2   | Tambah BahanBaku dengan kode `PJ999`                            | Ditolak                          |
| 3   | Tambah barang dengan kode yang sudah ada                        | Ditolak                          |
| 4   | Tambah barang dengan nama kosong                                | Ditolak                          |
| 5   | Tambah barang dengan stok negatif                               | Ditolak                          |
| 6   | Tambah barang dengan harga beli 0                               | Ditolak                          |
| 7   | Tambah ProdukJadi dengan harga jual lebih kecil dari harga beli | Ditolak                          |
| 8   | Tambah BahanBaku dengan format tanggal salah                    | Ditolak                          |
| 9   | Cari barang berdasarkan kode                                    | Barang ditemukan                 |
| 10  | Cari barang berdasarkan nama sebagian                           | Barang ditemukan                 |
| 11  | Ubah nama barang                                                | Berhasil                         |
| 12  | Ubah stok barang                                                | Berhasil                         |
| 13  | Ubah atribut khusus BahanBaku                                   | Berhasil                         |
| 14  | Hapus barang lalu memilih `n` pada konfirmasi                   | Penghapusan dibatalkan           |
| 15  | Hapus barang lalu memilih `y` pada konfirmasi                   | Barang berhasil dihapus          |
| 16  | Tutup aplikasi lalu buka kembali                                | Data tetap tersedia              |
| 17  | Laporan total stok                                              | Total stok tampil                |
| 18  | Laporan nilai inventaris                                        | Total nilai inventaris tampil    |
| 19  | Laporan stok rendah                                             | Barang dengan stok rendah tampil |
| 20  | Laporan jumlah jenis barang                                     | Jumlah barang per jenis tampil   |

---

## 14. Class yang Digunakan

| No  | Class             | Jenis               | Penjelasan                         |
| --- | ----------------- | ------------------- | ---------------------------------- |
| 1   | `ItemInterface`   | Abstract Base Class | Antarmuka dasar untuk semua barang |
| 2   | `Barang`          | Superclass          | Menyimpan atribut umum barang      |
| 3   | `BahanBaku`       | Subclass            | Barang berupa bahan baku cafe      |
| 4   | `ProdukJadi`      | Subclass            | Barang berupa produk siap jual     |
| 5   | `PeralatanCafe`   | Subclass            | Barang berupa peralatan cafe       |
| 6   | `BarangKemasan`   | Subclass            | Barang berupa kemasan cafe         |
| 7   | `ValidasiMixin`   | Mixin               | Menyediakan fungsi validasi        |
| 8   | `LoggableMixin`   | Mixin               | Menyediakan fungsi log aktivitas   |
| 9   | `ManajemenBarang` | Service             | Mengelola CRUD barang              |
| 10  | `LaporanStok`     | Service             | Membuat laporan stok               |
| 11  | `JsonStorage`     | Service             | Menyimpan dan membaca data JSON    |
| 12  | `DisplayHelper`   | Utility             | Mengatur tampilan CLI              |

---

## 15. Relasi Antar Class

Relasi utama antar class:

```text
ItemInterface
      ↑
    Barang
      ↑
 ┌───────────────┬───────────────┬────────────────┬────────────────┐
 BahanBaku       ProdukJadi      PeralatanCafe     BarangKemasan
```

Relasi service:

```text
ManajemenBarang menggunakan objek Barang
LaporanStok menggunakan daftar objek Barang
JsonStorage menyimpan dan membaca objek Barang
DisplayHelper membantu tampilan aplikasi
ValidasiMixin digunakan untuk validasi data
LoggableMixin digunakan untuk mencatat aktivitas
```

---

## 16. Ketentuan Project

Project ini dibuat dengan beberapa ketentuan:

1. Aplikasi dijalankan melalui terminal atau command prompt.
2. Aplikasi menggunakan bahasa pemrograman Python.
3. Aplikasi menerapkan paradigma Object-Oriented Programming.
4. Setiap class utama dipisahkan ke file berbeda.
5. Data barang tidak diubah langsung, tetapi melalui method yang disediakan class.
6. Data barang disimpan menggunakan file JSON.
7. Program harus dapat menangani input yang tidak valid.
8. Program harus menampilkan pesan error yang jelas.
9. Program harus memiliki struktur folder yang rapi.
10. Program harus memiliki UML Class Diagram yang sesuai dengan kode.
11. Program harus dapat dijelaskan melalui video presentasi.

---

## 17. Kelebihan Aplikasi

Beberapa kelebihan dari aplikasi ini:

1. Struktur kode modular dan mudah dikembangkan.
2. Menggunakan konsep OOP secara jelas.
3. Data tersimpan secara permanen menggunakan JSON.
4. Validasi input menjaga konsistensi data.
5. Tampilan CLI dibuat lebih rapi dan mudah digunakan.
6. Setiap jenis barang memiliki atribut dan perilaku khusus.
7. Polymorphism dapat terlihat dari method `tampilkan_info()` dan `to_dict()`.
8. Cocok untuk studi kasus inventaris cafe.

---

## 18. Batasan Aplikasi

Aplikasi ini memiliki beberapa batasan:

1. Aplikasi masih berbasis CLI.
2. Belum menggunakan database seperti MySQL atau SQLite.
3. Belum memiliki sistem login.
4. Belum memiliki fitur transaksi penjualan.
5. Belum memiliki fitur export laporan ke PDF atau Excel.
6. Data hanya disimpan dalam file JSON lokal.

Batasan ini dibuat agar aplikasi tetap fokus pada tujuan utama tugas, yaitu penerapan konsep OOP dalam pengelolaan data barang.

---

## 19. Rencana Pengembangan

Jika aplikasi dikembangkan lebih lanjut, fitur yang dapat ditambahkan adalah:

1. Sistem login untuk Admin, Petugas Gudang, dan Manajer.
2. Database SQLite atau MySQL.
3. Export laporan ke PDF atau Excel.
4. Dashboard berbasis GUI atau web.
5. Riwayat perubahan stok.
6. Fitur transaksi penjualan.
7. Fitur notifikasi barang hampir habis.
8. Fitur notifikasi bahan baku hampir kedaluwarsa.

---

## 20. Kesimpulan

TIF Cafe Inventory System merupakan aplikasi inventaris cafe berbasis CLI yang menerapkan konsep OOP secara terstruktur. Aplikasi ini menggunakan enkapsulasi untuk melindungi data, abstraksi melalui Abstract Base Class, mixins untuk fungsi tambahan, inheritance untuk relasi antar class, polymorphism untuk perilaku berbeda pada setiap jenis barang, serta modularitas agar kode lebih rapi dan mudah dikembangkan.

Dengan fitur pengelolaan barang, laporan stok, validasi input, dan penyimpanan JSON, aplikasi ini memenuhi kebutuhan utama dalam pengelolaan inventaris sederhana pada cafe.
