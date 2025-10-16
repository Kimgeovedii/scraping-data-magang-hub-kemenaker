# 🧠 Scraper Data Peserta MagangHub

Skrip **Python** ini dirancang untuk melakukan _scraping_ data detail peserta dari platform **MagangHub Kemnaker** secara otomatis.  
Tujuannya adalah untuk mengumpulkan data portofolio dari banyak peserta dan menyajikannya dalam satu file **Excel** yang rapi dan _flattened_ agar mudah dianalisis.

---

## ✨ Fitur Utama

- ⚡ **Scraping Paralel** — Menggunakan _multithreading_ untuk mengambil data dari beberapa peserta secara bersamaan, membuat proses jauh lebih cepat.
- 📊 **Output Excel** — Menghasilkan file `.xlsx` yang bersih, di mana setiap baris mewakili satu item portofolio (pendidikan, pengalaman, dll).
- 🧩 **Konfigurasi Mudah** — Cukup perbarui `HEADERS` dan endpoint untuk menyesuaikan dengan sesi login atau target data Anda.
- ⏳ **Progress Bar Interaktif** — Dilengkapi dengan _progress bar_ (tqdm) untuk memantau proses scraping secara real-time.

---

## ⚠️ Peringatan Penting (Mohon Dibaca)

> **Etika & Hukum**  
> Skrip ini mengakses data yang memerlukan login. Pengguna bertanggung jawab penuh atas penggunaan skrip ini secara **etis** dan **mematuhi hukum yang berlaku**, termasuk **UU Perlindungan Data Pribadi (UU PDP)**.  
> Jangan menyebarluaskan data pribadi yang Anda dapatkan.

> **Risiko Diblokir**  
> Penggunaan skrip secara berlebihan atau terlalu cepat dapat menyebabkan akun atau alamat IP Anda **diblokir sementara** oleh server. Gunakan dengan bijak.

> **Tujuan Edukasi**  
> Skrip ini dibuat hanya untuk **tujuan edukasi dan penelitian**.  
> Penulis tidak bertanggung jawab atas penyalahgunaan apa pun.

---

## 🚀 Cara Penggunaan

## Berikut langkah-langkah untuk menyiapkan dan menjalankan skrip ini.

### 1️⃣ Prasyarat

Pastikan Anda sudah menginstal:

- **Python 3.8** atau versi lebih baru
- **pip** (manajer paket Python)

---

### 2️⃣ Instalasi

---

Clone repositori ini ke komputer lokal Anda:

```bash
git clone https://github.com/Kimgeovedii/scraping-data-magang-hub-kemenaker.git
cd scraping-data-magang-hub-kemenaker
```

Instal semua dependensi yang dibutuhkan:

```
pip install -r requirements.txt

```

---

### 3️⃣ Konfigurasi (Langkah Paling Penting)

---

Sebelum menjalankan skrip, Anda wajib mengonfigurasi HEADERS untuk menyertakan token autentikasi.

Langkah Mendapatkan Token:

Login ke akun Anda di MagangHub
.

Buka Developer Tools di browser (F12 atau Ctrl+Shift+I).

Buka tab Network.

Lakukan aksi yang memicu permintaan API (misalnya klik tombol Detail Peserta).

Cari permintaan terkait seperti crud-users, portofolio-pendidikan, dll.

Klik kanan → Copy → Copy as cURL (bash).

Buka curlconverter.com
dan ubah cURL menjadi Python dictionary.

Salin hasilnya dan tempel di file scrape_data.py, ganti isi dari variabel HEADERS = { ... }.

🧠 Catatan Penting:
Token di dalam 'Authorization': 'Bearer ey...' memiliki masa berlaku terbatas.
Jika skrip berhenti (misalnya error 401 Unauthorized), ulangi langkah di atas untuk memperbarui token.

---

### 4️⃣ Jalankan Skrip

---

Setelah semua konfigurasi selesai, jalankan skrip dengan perintah:

```
python scrape_data.py

```

Skrip akan:

Mengambil daftar ID peserta

Mengambil detail portofolio tiap peserta secara paralel

Menampilkan progress bar agar Anda tahu sejauh mana proses berjalan

---

### 5️⃣ Hasil Output

---

Setelah selesai, sebuah file bernama:

```
hasil_data_peserta.xlsx

```

akan muncul di folder yang sama.
File ini berisi data portofolio peserta dalam format tabel yang siap dianalisis menggunakan Excel, Power BI, atau alat analisis lainnya.

---

### 📦 Dependensi Utama

requests

tqdm

pandas

openpyxl

concurrent.futures

Semua sudah tercantum di file requirements.txt.

---

### 💡 Kontribusi

---

Pull request dan perbaikan selalu diterima.
Jika Anda ingin menambah fitur (misalnya logging, retry system, atau scraping tambahan), silakan buat branch baru dan ajukan PR.

---

### 🧾 Lisensi

Proyek ini dirilis di bawah lisensi MIT License — silakan digunakan dan dimodifikasi dengan tetap memperhatikan etika dan hukum yang berlaku.

Dibuat dengan oleh @Kimgeovedii
