from google_play_scraper import reviews, Sort
from database_connector import save_data
import time

print("Memulai misi pengambilan 50.000 data Gojek...")
batch_size = 1000
total_target = 50000
continuation_token = None

for i in range(0, total_target, batch_size):
    print(f"Mengambil batch ke-{i // batch_size + 1} (Total data sekarang: {i})...")
    
    try:
        result, continuation_token = reviews(
            'com.gojek.app',
            lang='id',
            country='id',
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=continuation_token
        )
        
        if result:
            save_data("review_gojek", result)
            
        if not continuation_token:
            print("Data dari server sudah habis.")
            break
            
        time.sleep(3) # Jeda 3 detik agar tidak diblokir Google
    except Exception as e:
        print(f"Terjadi kendala: {e}. Melanjutkan setelah jeda...")
        time.sleep(10)

print("Proses Ingestion 50.000 data selesai!")