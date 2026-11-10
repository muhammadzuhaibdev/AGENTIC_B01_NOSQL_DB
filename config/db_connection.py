import os
from pymongo import MongoClient

def dbConnection():
    try:
        output = MongoClient(os.getenv("DB_URI"))
        print("MongoDb connected Successfully!")
        return output
    except Exception as e:
        print("Error connecting Mongodb", e)


client = dbConnection()
db = client["aztec-b01"]