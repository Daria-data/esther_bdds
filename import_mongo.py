from pymongo import MongoClient
import json
import os
from config import MONGO_CONFIG

# Connect to MongoDB
client = MongoClient(MONGO_CONFIG["mongo_uri"])
db = client[MONGO_CONFIG["database_name"]]

# Récupérer les fichiers json
path = 'data/data_json/data-json/'
files = os.listdir(path)
print(files)

for file in files:
    if file.endswith('.json'):
        collection = db[file.split('.')[0]]
        # Insert les données depuis le fichier json
        with open(f'data/data_json/data-json/{file}') as f:
            data = json.load(f)
            collection.insert_many(data)
            print(f"Data from {file} inserted")

# Close the connection
client.close()
print("Connexion closed")
print("Done!")