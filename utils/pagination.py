import requests
import time
from .logger import logger
from config import BASE_URL, HEADERS, RATE_LIMIT

def fetch_all_pages(endpoint):
    all_data = []
    page = 1

    while True:
        url = f"{BASE_URL}{endpoint}&page={page}"
        logger.info(f"Mengambil halaman {page}: {url}")
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            items = data.get("data", [])
            if not items:
                break
            all_data.extend(items)
            logger.info(f"Berhasil mengambil {len(items)} data di halaman {page}. Total sejauh ini: {len(all_data)}")
            page += 1
            time.sleep(RATE_LIMIT)
        except Exception as e:
            logger.error(f"Gagal mengambil halaman {page}: {e}")
            break

    return all_data
