import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
MASTER_LIST_ENDPOINT = os.getenv("MASTER_LIST_ENDPOINT")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
COOKIE_TOKEN = os.getenv("COOKIE_TOKEN")

HEADERS =  {
  'accept': 'application/json',
  'accept-language': 'id,en-US;q=0.9,en;q=0.8',
  'authorization': AUTH_TOKEN,
  'Cookie': COOKIE_TOKEN
}

MASTER_LIST_ENDPOINT = MASTER_LIST_ENDPOINT
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
RATE_LIMIT = 0.3  # waktu delay antar request (detik)
