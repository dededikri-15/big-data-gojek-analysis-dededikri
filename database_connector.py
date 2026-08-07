from pymongo import MongoClient

def get_db():
    # Ini adalah "kunci" pembuka pintu ke MongoDB Anda
    client = MongoClient("mongodb://localhost:27017/")
    return client["proyek_big_data"]

def save_data(collection_name, data):
    db = get_db()
    collection = db[collection_name]
    if data:
        collection.insert_many(data)
        print(f"Berhasil menyimpan {len(data)} data ke: {collection_name}")