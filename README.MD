# 🕵️‍♂️ Scraper Data Peserta MagangHub

Skrip Python ini dirancang untuk melakukan **scraping data detail peserta** dari platform [MagangHub Kemnaker](https://maganghub.kemnaker.go.id/) secara otomatis.  
Tujuannya adalah untuk **mengumpulkan data portofolio peserta** dan menyajikannya dalam satu file Excel yang rapi dan "rata" (flattened) untuk kemudahan analisis.

---

## ✨ Fitur Utama
- ⚡ **Scraping Paralel**: Menggunakan multithreading agar proses scraping jauh lebih cepat.  
- 📊 **Output Excel**: Menghasilkan file `.xlsx` bersih dan mudah dibaca.  
- ⚙️ **Konfigurasi Mudah**: Cukup ubah `HEADERS` & endpoint sesuai sesi login Anda.  
- 📈 **Progress Bar**: Memantau progres scraping secara real-time dengan `tqdm`.

---

## 📚 Dokumentasi Lengkap

| File | Deskripsi |
|------|------------|
| [docs/01_overview.md](docs/01_overview.md) | Gambaran umum proyek |
| [docs/02_installation.md](docs/02_installation.md) | Panduan instalasi & dependensi |
| [docs/03_configuration.md](docs/03_configuration.md) | Cara konfigurasi `HEADERS` |
| [docs/04_usage.md](docs/04_usage.md) | Cara menjalankan skrip & hasil output |
| [docs/05_warnings.md](docs/05_warnings.md) | Etika, batasan, dan peringatan penting |

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Kimgeovedii/scraping-data-magang-hub-kemenaker.git

cd scraping-data-magang-hub-kemenaker

# Install dependensi
pip install -r requirements.txt

# Jalankan scraper
python scrape_data.py
```

Hasil scraping akan muncul di folder `output/` dengan nama:
```
hasil_data_peserta.xlsx
```

---

## ⚠️ Peringatan Penting
> **Gunakan skrip ini secara etis dan bertanggung jawab.**
>
> Data yang diambil memerlukan autentikasi. Pastikan Anda mematuhi hukum yang berlaku, termasuk **UU Pelindungan Data Pribadi (UU PDP)**.  
> Skrip ini dibuat untuk **tujuan edukasi dan penelitian**, bukan untuk komersialisasi atau distribusi data.

---

## 🧑‍💻 Kontribusi
Pull Request sangat diterima!  
Jika Anda ingin menambahkan fitur, dokumentasi, atau optimasi performa, silakan buat branch baru dan ajukan PR.

---

## 🪪 Lisensi
Proyek ini dilisensikan di bawah lisensi **MIT License** — silakan gunakan, modifikasi, dan distribusikan dengan tetap mencantumkan kredit.

---

## 📬 Kontak
**Author:** [Mohamad Mustofa Hakim](https://github.com/Kimgeovedii)  
**Tujuan:** Edukasi & penelitian scraping data publik
