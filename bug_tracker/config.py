import pymongo
import os
# Provide the mongodb localhost url to connect python to mongodb.

mongo_client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
