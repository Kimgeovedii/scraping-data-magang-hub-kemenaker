# 🔧 Konfigurasi

Sebelum menjalankan skrip, ubah bagian `HEADERS` di `scrape_data.py`.

1. Login ke akun MagangHub.
2. Buka **Developer Tools (F12)** > tab **Network**.
3. Lakukan aksi di situs (mis. buka 'Detail Peserta').
4. Klik kanan request → **Copy as cURL (bash)**.
5. Gunakan [curlconverter.com](https://curlconverter.com) untuk ubah menjadi Python dict.
6. Tempel hasilnya ke variabel `HEADERS = {...}` di `scrape_data.py`.

> 🧠 Catatan: Token Authorization bersifat sementara. Jika error `401 Unauthorized`, ambil token baru.
