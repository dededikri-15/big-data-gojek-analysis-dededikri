# 🟢 Pengelolaan Big Data pada Log Transaksi dan Media Teks Ulasan Pengguna Aplikasi Gojek

Proyek analisis **Big Data Management** yang berfokus pada perancangan arsitektur, ekstraksi, penyimpanan, pembersihan, dan visualisasi 50.000 data ulasan serta log transaksi pengguna aplikasi Gojek dari Google Play Store.

---

## 🎯 Tujuan Proyek

1. **Penyimpanan Terstruktur:** Menerapkan sistem penyimpanan data menggunakan MongoDB yang mampu menampung dan mengelola 50.000 media teks ulasan serta log transaksi pengguna Gojek secara terstruktur.
2. **Analisis Pola Perilaku:** Menganalisis ulasan dan log transaksi untuk mengidentifikasi pola perilaku, kebutuhan, serta tingkat kepuasan pengguna.
3. **Rancangan Arsitektur:** Merancang arsitektur dan diagram fungsional sistem Big Data Management yang ideal untuk pemrosesan data secara efektif[cite: 2].

---

## ⚡ Karakteristik Big Data (5V Implementation)

* **Volume:** Mengelola kumpulan **50.000 data ulasan** pengguna aplikasi Gojek[cite: 2].
* **Variety:** Terdiri dari data terstruktur dari *Log Transaksi* (`score`, `appVersion`, `at`) dan data tidak terstruktur dari *Media Teks* (`content`)[cite: 2].
* **Velocity:** Pengumpulan data ulasan otomatis dari server Google Play Store melalui proses *crawling* bertahap secara cepat[cite: 2].
* **Veracity:** Proses pembersihan (*Data Cleaning*) menggunakan Pandas untuk menjamin keakuratan dan keandalan data[cite: 2].
* **Value:** Mengubah data mentah menjadi wawasan bisnis untuk peningkatan kualitas layanan Gojek[cite: 2].

---

## 🏗️ Design & Arsitektur Big Data Management

### 1. Rancangan Arsitektur Big Data

<div align="center">
  <img width="630" alt="Rancangan Arsitektur Big Data Management" src="https://github.com/user-attachments/assets/2b3cf8ef-3a07-4e5e-a5ad-f705f8ed0245" />
  <p><i>Gambar 1: Rancangan Arsitektur Big Data Management</i></p>
</div>

**Penjelasan Alur Arsitektur:**
1. **Google Play Store (Ulasan Pengguna):** Sumber data utama yang menyediakan ulasan pengguna aplikasi Gojek beserta rating, timestamp, dan versi aplikasi[cite: 2].
2. **Python + Google-Play-Scraper (Crawling):** Mengambil data ulasan secara otomatis dari server Google Play Store secara bertahap[cite: 2].
3. **MongoDB (Data Storage):** Tempat penyimpanan utama berbasis NoSQL untuk menampung seluruh data mentah hasil crawling[cite: 2].
4. **Pandas (Data Cleaning & Processing):** Membersihkan data dari nilai null dan duplikat ulasan[cite: 2].
5. **cleaning_data.csv:** Dataset hasil pembersihan yang siap digunakan untuk analisis[cite: 2].
6. **Power BI (Dashboard & Visualisasi Data):** Mengolah dataset bersih menjadi dasbor interaktif[cite: 2].
7. **Informasi (Hasil Analisis):** Menghasilkan wawasan berupa distribusi rating, tren ulasan, dan kepuasan pengguna[cite: 2].

---

### 2. Pengecekan Data pada MongoDB Compass

<div align="center">
  <img width="902" alt="Verifikasi Data MongoDB Compass" src="https://github.com/user-attachments/assets/75d4755b-e044-4b81-bb80-c21359697fca" />
  <p><i>Gambar 2: Verifikasi 50.000 Data Bersih di MongoDB Compass</i></p>
</div>

*Pengecekan koleksi `review_gojek_clean` pada database `proyek_big_data` melalui MongoDB Compass untuk memastikan 50.000 dokumen ulasan tersimpan terstruktur dengan atribut JSON lengkap (`reviewId`, `userName`, `content`, `score`, `appVersion`, dll)*[cite: 2].

---

### 3. Diagram Fungsional Big Data

<div align="center">
  <img width="485" alt="Diagram Fungsional Big Data Management" src="https://github.com/user-attachments/assets/7e4ad147-cb9e-4e03-b1ed-84092e79a920" />
  <p><i>Gambar 3: Diagram Fungsional Big Data Management (Konsep 5V)</i></p>
</div>

**Tahapan Fungsi Sistem:**
* **Input (Velocity):** Mengambil 50.000 ulasan dari Play Store secara otomatis dan cepat[cite: 2].
* **Penyimpanan (Volume):** Menampung data berskala besar ke dalam database NoSQL MongoDB[cite: 2].
* **Pengolahan (Variety & Veracity):** Membersihkan ulasan kosong (`content`) dan duplikat (`reviewId`) menggunakan Pandas[cite: 2].
* **Output (Value):** Menyajikan grafik visualisasi interaktif dan wawasan evaluasi layanan melalui Power BI[cite: 2].

---

## 📊 Analisis & Visualisasi Data (Power BI)

<div align="center">
  <img width="976" alt="Dashboard Analisis Power BI" src="https://github.com/user-attachments/assets/08fbb985-0a68-4014-b09a-5dc3be833d18" />
  <p><i>Gambar 4: Dasbor Analisis Keseluruhan pada Power BI</i></p>
</div>

**Fokus Visualisasi:**
1. **Tingkat Kepuasan Pengguna (Skor Bintang):** Memetakan rasio ulasan positif (skor 5) dibandingkan ulasan negatif (skor 1)[cite: 2].
2. **Tren Aktivitas Ulasan Pengguna:** Memantau fluktuasi jumlah ulasan pengguna dari waktu ke waktu[cite: 2].
3. **Perbandingan Rata-Rata Kepuasan per Versi Aplikasi:** Mengevaluasi stabilitas teknis dari setiap update `appVersion`[cite: 2].
4. **Volume Pergerakan Ulasan:** Visualisasi kepadatan data interaksi pengguna[cite: 2].
5. **Daftar Kontribusi Ulasan Pengguna:** Menunjukkan tingkat keterlibatan pengguna dalam memberikan masukan[cite: 2].
6. **Ulasan Paling Bermanfaat:** Menyoroti opini pengguna yang memiliki nilai `thumbsUpCount` tertinggi[cite: 2].

---

## 🎨 Rancangan Tampilan Antarmuka (UI Dashboard Canva)

<div align="center">
  <img width="1018" alt="Rancangan Tampilan UI Dashboard" src="https://github.com/user-attachments/assets/fbd6069c-ecea-4932-bef8-04c959c9f0bf" />
  <p><i>Gambar 5: Rancangan Tampilan Antarmuka (UI) Dashboard Analisis Ulasan Pengguna Gojek</i></p>
</div>

🔗 **[Lihat Desain UI Dashboard Interaktif di Canva](https://canva.link/fiwt54ckqc642mh)**[cite: 2]

---

## 🛠️ Alat dan Teknologi

* **Bahasa Pemrograman:** Python[cite: 2]
* **IDE:** Visual Studio Code (VS Code)[cite: 2]
* **Database (NoSQL):** MongoDB & PyMongo[cite: 2]
* **Library Processing:** Pandas & `google-play-scraper`[cite: 2]
* **Business Intelligence:** Power BI[cite: 2]
* **Diagram & UI Design:** Draw.io, Figma, & Canva[cite: 2]

---

## 📁 Struktur Berkas Repositori

```text
├── crawling_gojek.py        # Skrip Python untuk crawling 50.000 data dari Play Store
├── database_connector.py    # Skrip koneksi penghubung Python ke MongoDB
├── data_processor.py        # Skrip pembersihan data (menghapus null & duplikat)
├── cleaning_data.csv        # Dataset bersih hasil pembersihan
└── README.md                # Dokumentasi proyek


💻 Penjelasan Skrip Python
1. database_connector.py
Skrip penghubung (konektor) antara Python dengan database MongoDB lokal[cite: 2].

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
Skrip ekstraksi data ulasan dari Google Play Store secara otomatis menggunakan batching 1.000 data[cite: 2].

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
Skrip pembersihan (Data Cleaning) untuk menghapus ulasan kosong (dropna), menghapus duplikasi berdasarkan reviewId (drop_duplicates), serta mengekspor hasil ke cleaning_data.csv[cite: 2].

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

