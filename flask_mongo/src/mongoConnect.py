from pymongo import MongoClient
# connect mongodb client

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.mymongodb #Select the database