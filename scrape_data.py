import requests
import pandas as pd
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


BASE_URL = "https://maganghub.kemnaker.go.id/be/v1/api/"
HEADERS = {
  'accept': 'application/json',
  'accept-language': 'id,en-US;q=0.9,en;q=0.8',
  'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YzVlZTk2Yi04MzcwLTQzYTMtOTRjZi0yZDVhYTg1ZDIxZmUiLCJqdGkiOiJkNmUzMjMyYTJiODhmZWY2M2E1MDdmMTk3NDQ5NDI2MDJlZTAwNDNkNmNiZjhiZjAwMzY4NGNlNmE4M2QyZjg5N2NlYTIzOWIyYjE4MDRlMCIsImlhdCI6MTc2MDU3NTQyMS4wOTk4NzcsIm5iZiI6MTc2MDU3NTQyMS4wOTk4NzksImV4cCI6MTc5MjExMTQyMS4wOTQ3MDksInN1YiI6IjY0ZjI1MjlhLWNjMGMtNDU1YS05MDBlLTk3ZWRlMzA0M2MyNCIsInNjb3BlcyI6W119.iJsp_xwHpSwf-SE8r5PnNJN79eUtKwsKDR8m_PeKGqYIGhXUFo6U_bXpmI_LDj1x_6vVUa5eklSeKakkIH-jU1EVW58prHvGyuFt1hEAmhVlMkF5k0XTUBW9iJZnXOvAOTWHlWaOG7gmceCLmSYiIzU3gUOrHma6c-oH5HmTCFrst-jGedLbeVoJDrgEWv5TIY348momUML9r-yTpwjFHnY0oI0YRG-rIm8U8SvYPspzvve_QmphXeey2jovvEbnMe67rwHDoDFHR31st0Vfof0yvghZ8pkznZ_qIhNUth6vMCiQHujdZ0KH7S_zvm2MFlwUIjyrACTKUj0m7h7RWtIP8tMvYb4FBqWdCT88Z6hFU3xaUIUgYdUg80i8Du0ZjwBvSQ5Cu7DlLlTXP0vNyKdX8dSfAxTOaXDwxu_ZoVtgTnsZTBBO9344qneFwXB3ZgrIpRmHYASKerIHPNS5kVvO9t3hYmKM4YMz0m18ZhVLIw25y8D5aXyvDbaIC2G0pghYTaC4BKLaRkHa9cqY61O2zKunB37ccZvJXDlyFw39kkjsR6EQGstz1CiOieXn_SCpAeL5_-xjODuFBlNt85Blh1mw1YAQOrLtManMo0hsL2ajHuyPMHAsR5AZI9HdTEOPZh6-iqmR-9aZpGaaVuIJk3kw0uBZtlAX5-sXpK8',
  'Cookie': 'acw_tc=0a03087517605962181225763e7ab443224e412dd7920252b10bd7b9071891'
}

MASTER_LIST_ENDPOINT = "program-posisis/3afbefe6-faf4-4f02-b819-3b3f9c17c45a/program-pesertas?order_by=tanggal_daftar&order_direction=ASC&page=1&limit=150&per_page=150"
DETAIL_ENDPOINTS = {
    'user_info': 'crud-users',
    'pendidikan': 'portofolio-pendidikan',
    'pelatihan': 'portofolio-pelatihan',
    'sertifikasi': 'portofolio-sertifikasi',
    'pengalaman': 'portofolio-pengalaman',
    'keterampilan': 'portofolio-keterampilan',
    'bahasa': 'portofolio-bahasa'
}

MAX_WORKERS = 10

def get_all_user_ids():
    url = f"{BASE_URL}{MASTER_LIST_ENDPOINT}"
    print(f"Mengambil daftar ID dari: {url}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        ids = [item['id'] for item in data['data']]
        print(f"Berhasil mendapatkan {len(ids)} ID pengguna.")
        return ids
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil daftar ID: {e}\nResponse: {response.text}")
        return []

def get_user_raw_data(user_id):
    user_raw_data = {}
    for key, endpoint in DETAIL_ENDPOINTS.items():
        url = f"{BASE_URL}list/{endpoint}?id={user_id}"
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            user_raw_data[key] = response.json().get('data', None)
            time.sleep(0.2)
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            user_raw_data[key] = None
    return user_id, user_raw_data

def process_and_flatten_data(user_id, raw_data):
    flattened_rows = []
    user_info_raw = raw_data.get('user_info')
    user_info = None
    if isinstance(user_info_raw, list) and len(user_info_raw) > 0:
        user_info = user_info_raw[0]
    elif isinstance(user_info_raw, dict):
        user_info = user_info_raw

    if not user_info: return []
        
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
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_id = {executor.submit(get_user_raw_data, uid): uid for uid in all_ids}
            
            for future in tqdm(as_completed(future_to_id), total=len(all_ids), desc="Scraping Data Peserta"):
                try:
                    user_id, raw_data = future.result()
                    processed_rows = process_and_flatten_data(user_id, raw_data)
                    all_flattened_data.extend(processed_rows)
                except Exception as exc:
                    print(f"ID {future_to_id[future]} menyebabkan error: {exc}")

        print("\nMenyimpan semua data ke file CSV...")
        df = pd.DataFrame(all_flattened_data)
        output_filename = 'ODS_Business_Support.xlsx' 
        df.to_excel(output_filename, index=False)    
        print(f"Selesai! Data tersimpan di file '{output_filename}'")