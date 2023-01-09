import pymongo

client = pymongo.MongoClient("mongodb://tests_python:FdpqmEtaXkkM2Iqx@ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017,ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017,ac-mbprgjx-shard-00-01.mbzev6i.mongodb.net:27017/?authMechanism=DEFAULT&authSource=admin&tls=true")
db = client.pruebas
db = client["pruebas"]
users_collection = db["users"]
users_collection_token = db["token_temp"]
users_collection_addToLayaway = db["pruebas.addToLayaway"]

