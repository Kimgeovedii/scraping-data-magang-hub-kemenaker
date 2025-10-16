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

3. Buka file `config.py` dan isi:
   - `HEADERS['authorization']` → token Bearer kamu
   - `MASTER_LIST_ENDPOINT` → endpoint peserta (tanpa page)
     Contoh:
     ```python
     MASTER_LIST_ENDPOINT = "program-posisis/xxxxxx/program-pesertas?order_by=tanggal_daftar&order_direction=ASC&limit=150&per_page=150"
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
