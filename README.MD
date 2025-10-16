# MagangHub Scraper (Final Version)

## 📦 Struktur Folder

```
scraper-final/
├── scrape_data.py
├── config.py
├── utils/
│   ├── logger.py
│   └── pagination.py
├── logs/
│   └── scraper.log
├── requirements.txt
└── README.md
```

## ⚙️ Persiapan

1. Pastikan Python >= 3.9 sudah terinstall.
2. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```

3. Isi file `.env` dengan informasi autentikasi API:

   - `AUTH_TOKEN` → token Bearer kamu
   - `MASTER_LIST_ENDPOINT` → endpoint peserta (tanpa page)
     Contoh:
     ```python
     MASTER_LIST_ENDPOINT = "program-posisis/xxxxxx/program-pesertas?order_by=tanggal_daftar&order_direction=ASC&limit=150&per_page=150"
     ```
   - `COOKIE_TOKEN`= Token Cookie Kamu

     ```

     ```

## 🚀 Cara Menjalankan

```bash
python scrape_data.py
```

Data akan otomatis:

- Mengambil semua halaman (pagination otomatis)
- Membatasi kecepatan scraping dengan delay kecil (`RATE_LIMIT`)
- Menyimpan hasil ke file `hasil_data_peserta.xlsx`
- Menulis log detail ke `logs/scraper.log`

## 🧾 Log Detail

File `logs/scraper.log` berisi catatan proses seperti:

```
2025-10-16 14:15:10 - INFO - Mengambil halaman 1: ...
2025-10-16 14:15:11 - INFO - Berhasil ambil data pendidikan untuk user_id=abcd
2025-10-16 14:15:15 - ERROR - Gagal ambil data sertifikasi untuk user_id=efgh: Timeout
```

## 📤 Output

Hasil akhir akan tersimpan di file `hasil_data_peserta.xlsx` dengan format sama seperti versi sebelumnya.

---

## ⚠️ Peringatan Penting

Gunakan skrip ini secara **etis dan bertanggung jawab.**  
Data yang diambil **memerlukan autentikasi.** Pastikan Anda mematuhi hukum yang berlaku, termasuk **UU Pelindungan Data Pribadi (UU PDP).**  
Skrip ini dibuat untuk **tujuan edukasi dan penelitian**, **bukan untuk komersialisasi atau distribusi data.**
