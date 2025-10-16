import requests
import pandas as pd
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from utils.logger import logger
from utils.pagination import fetch_all_pages
from config import BASE_URL, HEADERS, MASTER_LIST_ENDPOINT, DETAIL_ENDPOINTS, MAX_WORKERS, RATE_LIMIT

def get_all_user_ids():
    logger.info("Memulai pengambilan seluruh ID peserta...")
    data = fetch_all_pages(MASTER_LIST_ENDPOINT)
    ids = [item['id'] for item in data]
    logger.info(f"Total {len(ids)} ID ditemukan.")
    return ids

def get_user_raw_data(user_id):
    user_raw_data = {}
    for key, endpoint in DETAIL_ENDPOINTS.items():
        url = f"{BASE_URL}list/{endpoint}?id={user_id}"
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            user_raw_data[key] = response.json().get('data', None)
            logger.info(f"Berhasil ambil data {key} untuk user_id={user_id}")
            time.sleep(RATE_LIMIT)
        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            user_raw_data[key] = None
            logger.error(f"Gagal ambil data {key} untuk user_id={user_id}: {e}")
    return user_id, user_raw_data

def process_and_flatten_data(user_id, raw_data):
    flattened_rows = []
    user_info_raw = raw_data.get('user_info')
    user_info = None
    if isinstance(user_info_raw, list) and len(user_info_raw) > 0:
        user_info = user_info_raw[0]
    elif isinstance(user_info_raw, dict):
        user_info = user_info_raw

    if not user_info:
        return []

    base_info = {
        'id_user': user_id, 'nama_peserta': user_info.get('nama'),
        'email_peserta': user_info.get('email'), 'telepon_peserta': user_info.get('telepon')
    }

    has_portfolio = False
    for category, data_items in raw_data.items():
        if category == 'user_info' or not data_items: continue
        has_portfolio = True
        if not isinstance(data_items, list): data_items = [data_items]

        for item in data_items:
            if not isinstance(item, dict): continue
            new_row = base_info.copy()
            new_row['kategori_portofolio'] = category.capitalize()
            new_row.update(item)
            flattened_rows.append(new_row)

    if not has_portfolio:
        base_info['kategori_portofolio'] = 'Informasi Dasar'
        flattened_rows.append(base_info)

    return flattened_rows

if __name__ == "__main__":
    all_ids = get_all_user_ids()

    if all_ids:
        all_flattened_data = []
        logger.info("Mulai scraping paralel data peserta...")

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_id = {executor.submit(get_user_raw_data, uid): uid for uid in all_ids}

            for future in tqdm(as_completed(future_to_id), total=len(all_ids), desc="Scraping Data Peserta"):
                try:
                    user_id, raw_data = future.result()
                    processed_rows = process_and_flatten_data(user_id, raw_data)
                    all_flattened_data.extend(processed_rows)
                except Exception as exc:
                    logger.error(f"ID {future_to_id[future]} menyebabkan error: {exc}")

        logger.info("Selesai scraping. Menyimpan hasil ke file Excel...")
        df = pd.DataFrame(all_flattened_data)
        output_filename = 'hasil_data_peserta.xlsx' 
        df.to_excel(output_filename, index=False)    
        logger.info(f"Selesai! Data tersimpan di file '{output_filename}'")
