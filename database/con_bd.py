import pymongo

client = pymongo.MongoClient("mongodb://tests_python:7Qbe45lUL186WIpH@ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017,ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017,ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017/?authMechanism=DEFAULT&authSource=admin&tls=true")
db = client.pruebas

db = client["pruebas"]
users_collection = db["users"]

