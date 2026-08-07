# 🟢 Pengelolaan Big Data pada Log Transaksi dan Media Teks Ulasan Pengguna Aplikasi Gojek

Proyek analisis **Big Data Management** yang berfokus pada perancangan arsitektur, ekstraksi, penyimpanan, pembersihan, dan visualisasi 50.000 data ulasan serta log transaksi pengguna aplikasi Gojek dari Google Play Store.

---

## 🎯 Tujuan Proyek

1. **Penyimpanan Terstruktur:** Menerapkan sistem penyimpanan data menggunakan MongoDB yang mampu menampung dan mengelola 50.000 media teks ulasan serta log transaksi pengguna Gojek secara terstruktur.
2. **Analisis Pola Perilaku:** Menganalisis ulasan dan log transaksi untuk mengidentifikasi pola perilaku, kebutuhan, serta tingkat kepuasan pengguna.
3. **Rancangan Arsitektur:** Merancang arsitektur dan diagram fungsional sistem Big Data Management yang ideal untuk pemrosesan data secara efektif.

---

## ⚡ Karakteristik Big Data (5V Implementation)

- **Volume:** Mengelola kumpulan **50.000 data ulasan** pengguna aplikasi Gojek.
- **Variety:** Terdiri dari data terstruktur dari _Log Transaksi_ (`score`, `appVersion`, `at`) dan data tidak terstruktur dari _Media Teks_ (`content`).
- **Velocity:** Pengumpulan data ulasan otomatis dari server Google Play Store melalui proses _crawling_ bertahap secara cepat.
- **Veracity:** Proses pembersihan (_Data Cleaning_) menggunakan Pandas untuk menjamin keakuratan dan keandalan data.
- **Value:** Mengubah data mentah menjadi wawasan bisnis untuk peningkatan kualitas layanan Gojek.

---

## 🏗️ Design & Arsitektur Big Data Management

### 1. Rancangan Arsitektur Big Data

![Rancangan Arsitektur Big Data Management](arsitektur.png)
_Gambar 1: Rancangan Arsitektur Big Data Management_

### 2. Pengecekan Data pada MongoDB Compass

![Memasukan File CSV Clean ke MongoDb](mongodb_compass.png)
_Gambar 2: Verifikasi 50.000 Data Bersih di MongoDB Compass_

### 3. Diagram Fungsional Big Data

![Diagram Fungsional Big Data Management](diagram_fungsional.png)
_Gambar 3: Diagram Fungsional Big Data Management (Konsep 5V)_

---

## 📊 Analisis & Visualisasi Data (Power BI)

![Dashboard Analisis Power BI](powerbi_dashboard.png)
_Gambar 4: Dasbor Analisis Keseluruhan pada Power BI_

**Fokus Analisis:**

1. **Tingkat Kepuasan Pengguna (Skor Bintang):** Memetakan tingkat kepuasan pelanggan secara keseluruhan.
2. **Tren Aktivitas Ulasan Pengguna:** Memantau fluktuasi jumlah ulasan dari waktu ke waktu.
3. **Perbandingan Rata-Rata Kepuasan per Versi Aplikasi:** Mengevaluasi kualitas teknis dari setiap update aplikasi.
4. **Volume Pergerakan Ulasan:** Visualisasi kepadatan interaksi pengguna.
5. **Daftar Kontribusi Ulasan Pengguna:** Menunjukkan proporsi keterlibatan pengguna.
6. **Ulasan Paling Bermanfaat:** Menyoroti opini pengguna yang memiliki `thumbsUpCount` tertinggi.

---

## 🎨 Rancangan Tampilan Antarmuka (UI Dashboard Canva)

![Rancangan Tampilan UI Dashboard](ui_canva.png)
_Gambar 5: Rancangan Tampilan Antarmuka (UI) Dashboard Analisis Ulasan Pengguna Gojek_

🔗 **[Lihat Desain UI Dashboard Interaktif di Canva](https://canva.link/fiwt54ckqc642mh)**

---

## 🛠️ Alat dan Teknologi

- **Bahasa Pemrograman:** Python
- **IDE:** Visual Studio Code (VS Code)
- **Database (NoSQL):** MongoDB & PyMongo
- **Library Processing:** Pandas & `google-play-scraper`
- **Business Intelligence:** Power BI
- **Diagram & UI Design:** Draw.io, Figma, & Canva

---

## 📁 Struktur Berkas Repositori

```text
├── crawling_gojek.py        # Skrip Python untuk crawling 50.000 data dari Play Store
├── database_connector.py    # Skrip koneksi penghubung Python ke MongoDB
├── data_processor.py        # Skrip pembersihan data (menghapus null & duplikat)
├── cleaning_data.csv        # Dataset bersih hasil pembersihan
├── arsitektur.png           # Gambar Arsitektur
├── mongodb_compass.png      # Gambar MongoDB Compass
├── diagram_fungsional.png   # Gambar Diagram Fungsional
├── powerbi_dashboard.png    # Gambar Dashboard Power BI
├── ui_canva.png             # Gambar UI Canva
└── README.md                # Dokumentasi proyek


💻 Penjelasan Skrip Python
1. database_connector.py
Skrip penghubung (konektor) antara Python dengan database MongoDB lokal.

Python
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    return client["proyek_big_data"]

def save_data(collection_name, data):
    db = get_db()
    collection = db[collection_name]
    if data:
        collection.insert_many(data)
        print(f"Berhasil menyimpan {len(data)} data ke: {collection_name}")
2. crawling_gojek.py
Skrip ekstraksi data ulasan dari Google Play Store secara otomatis menggunakan batching 1.000 data.

Python
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
            save_data("review_gojek_2", result)

        if not continuation_token:
            print("Data dari server sudah habis.")
            break

        time.sleep(3) # Jeda 3 detik agar tidak diblokir Google
    except Exception as e:
        print(f"Terjadi kendala: {e}. Melanjutkan setelah jeda...")
        time.sleep(10)

print("Proses Ingestion 50.000 data selesai!")
3. data_processor.py
Skrip pembersihan (Data Cleaning) untuk menghapus ulasan kosong (dropna), menghapus duplikasi berdasarkan reviewId (drop_duplicates), serta mengekspor hasil ke cleaning_data.csv.

Python
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
🚀 Cara Menjalankan Proyek di Komputer Lokal
Clone Repositori:

Bash
git clone [https://github.com/dededikri-15/big-data-gojek-analysis-dededikri.git](https://github.com/dededikri-15/big-data-gojek-analysis-dededikri.git)
cd big-data-gojek-analysis-dededikri
Install Dependensi Library Python:

Bash
pip install pymongo google-play-scraper pandas
Jalankan Proses Ingestion / Crawling Data:

Bash
python crawling_gojek.py
Jalankan Proses Data Cleaning:

Bash
python data_processor.py
```
