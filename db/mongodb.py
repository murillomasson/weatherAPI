from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_CLIENT_URI = os.getenv('MONGO_CLIENT_URI')

DB = "weather"
COLL = "cities"

client = MongoClient(MONGO_CLIENT_URI)


def insert_weather_data(data):
    if DB not in client.list_database_names():
        db = client[DB]
    else:
        db = client.get_database(DB)

    if COLL not in db.list_collection_names():
        coll = db[COLL]
    else:
        coll = db.get_collection(COLL)

    coll.insert_one(data)
