BASE_URL = "https://maganghub.kemnaker.go.id/be/v1/api/"

# Kosongkan bagian token, isi manual sebelum menjalankan
HEADERS = {
    'accept': 'application/json',
    'accept-language': 'id,en-US;q=0.9,en;q=0.8',
    'authorization': '',
    'Cookie': ''
}

MASTER_LIST_ENDPOINT = ""  # isi dengan endpoint program-peserta
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
