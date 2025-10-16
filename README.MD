# Scraper Data Peserta MagangHub

Skrip Python ini dirancang untuk melakukan scraping data detail peserta dari platform MagangHub Kemnaker secara otomatis. Tujuannya adalah untuk mengumpulkan data portofolio dari banyak peserta dan menyajikannya dalam satu file Excel yang rapi dan "rata" (flattened) untuk kemudahan analisis.

## ✨ Fitur Utama

- **Scraping Paralel**: Menggunakan multithreading untuk mengambil data dari beberapa peserta secara bersamaan, membuat prosesnya jauh lebih cepat.
- **Output Excel**: Menghasilkan file `.xlsx` yang bersih, di mana setiap baris mewakili satu item portofolio (pendidikan, pengalaman, dll.).
- **Konfigurasi Mudah**: Cukup perbarui `HEADERS` dan _endpoint_ untuk menyesuaikan dengan sesi login atau target data Anda.
- **Progress Bar**: Dilengkapi dengan progress bar (`tqdm`) untuk memantau proses scraping secara real-time.

---

## ⚠️ Peringatan Penting (Mohon Dibaca)

- **Etika & Hukum**: Skrip ini mengakses data yang memerlukan login. Pengguna bertanggung jawab penuh untuk menggunakan skrip ini secara etis dan mematuhi semua hukum yang berlaku, termasuk **Undang-Undang Pelindungan Data Pribadi (UU PDP)**. Jangan menyebarluaskan data pribadi yang Anda dapatkan.
- **Risiko Diblokir**: Penggunaan skrip secara berlebihan atau terlalu cepat dapat menyebabkan akun atau alamat IP Anda diblokir sementara oleh server. Gunakan dengan bijak.
- **Tujuan Edukasi**: Skrip ini dibuat untuk tujuan edukasi dan penelitian. Penulis tidak bertanggung jawab atas penyalahgunaan apa pun.

---

## 🚀 Cara Penggunaan

Berikut adalah langkah-langkah untuk menyiapkan dan menjalankan skrip ini.

### 1. Prasyarat

- **Python 3.8** atau versi lebih baru.
- **pip** (manajer paket Python).

### 2. Instalasi

Clone repositori ini ke komputer lokal Anda:

```bash
git clone https://github.com/Kimgeovedii/scraping-data-magang-hub-kemenaker.git

```

```
pip install -r requirements.txt

```

3. Konfigurasi (Langkah Paling Penting)
   Sebelum menjalankan skrip, Anda wajib mengonfigurasi HEADERS. Token ini berfungsi sebagai kunci akses Anda ke API.

Login ke akun Anda di MagangHub.

Buka Developer Tools di browser Anda (biasanya dengan menekan F12 atau Ctrl+Shift+I).

Klik tab Network.

Lakukan sebuah aksi di halaman web yang memicu permintaan API (misalnya, klik tombol "Detail Peserta"). Anda akan melihat daftar permintaan baru muncul di tab Network.

Cari salah satu permintaan yang relevan (misalnya, crud-users, portofolio-pendidikan, dll.).

Klik kanan pada permintaan tersebut, lalu pilih Copy > Copy as cURL (bash).

Buka file scrape_data.py dan temukan bagian HEADERS = { ... }.

Hapus seluruh isi HEADERS yang lama dan ganti dengan yang baru dari cURL Anda. Cara termudah adalah menggunakan konverter online seperti curlconverter.com untuk mengubah cURL menjadi dictionary Python, lalu salin hasilnya.

PENTING: Token di dalam 'Authorization': 'Bearer ey...' memiliki masa berlaku. Jika skrip berhenti bekerja (misalnya error 401), ulangi langkah ini untuk mendapatkan token baru.

4. Jalankan Skrip
   Setelah konfigurasi selesai, jalankan skrip melalui terminal:

Bash

python scrape_data.py
Skrip akan mulai mengambil daftar ID peserta, lalu mengambil detail untuk setiap peserta secara paralel. Anda akan melihat progress bar yang menunjukkan kemajuannya.

5. Hasil Output
   Setelah selesai, sebuah file bernama hasil_data_peserta.xlsx akan dibuat di folder yang sama. File ini berisi semua data portofolio peserta dalam format tabel yang siap untuk dianalisis.
