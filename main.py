import time
import json
import requests
from tqdm import tqdm
import logging
from config import API_BASE_URL, MASTER_LIST_ENDPOINT, DETAIL_ENDPOINT, RATE_LIMIT_DELAY, LOG_FILE

# Konfigurasi logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def scrape_master_list():
    all_data = []
    page = 1

    logging.info("Memulai scraping data master list...")

    while True:
        url = f"{API_BASE_URL}{MASTER_LIST_ENDPOINT}?page={page}"
        logging.info(f"Mengambil halaman {page}: {url}")
        
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Status code {response.status_code} di halaman {page}")
                break

            data = response.json()
            items = data.get("data", [])
            if not items:
                logging.info("Tidak ada data lagi. Scraping selesai.")
                break

            all_data.extend(items)
            logging.info(f"Berhasil mengambil {len(items)} data dari halaman {page}")

            page += 1
            time.sleep(RATE_LIMIT_DELAY)
        except Exception as e:
            logging.error(f"Error di halaman {page}: {e}")
            break

    return all_data

def main():
    result = scrape_master_list()

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    logging.info(f"Scraping selesai - total {len(result)} data disimpan di output.json")
    print(f"✅ Scraping selesai - total {len(result)} data disimpan di output.json")

if __name__ == "__main__":
    main()
