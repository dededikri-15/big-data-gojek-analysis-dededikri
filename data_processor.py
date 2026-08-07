import pandas as pd
from pymongo import MongoClient

def process_data():
    # 1. Koneksi ke MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["proyek_big_data"]
    collection = db["review_gojek"]

    # 2. Ambil data dari MongoDB ke dalam Pandas DataFrame
    print("Mengambil data dari MongoDB untuk diproses...")
    data = list(collection.find())
    df = pd.DataFrame(data)

    # 3. Data Cleaning (Proses Pembersihan)
    print("Memulai proses Data Cleaning...")
    # Hapus baris jika isi ulasan (content) kosong
    df = df.dropna(subset=['content'])
    # Hapus duplikat berdasarkan reviewId
    df = df.drop_duplicates(subset=['reviewId'])
    
    print(f"Data setelah dibersihkan: {len(df)} baris.")

    # 4. Simpan hasil bersih ke CSV untuk Power BI
    df.to_csv("cleaning_data.csv", index=False)
    print("Data bersih berhasil disimpan ke 'cleaning_data.csv'.")

if __name__ == "__main__":
    process_data()