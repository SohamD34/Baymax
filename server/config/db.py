import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# print(pymongo.__version__)

def load_credentials():
    try:
        load_dotenv()
        MONGODB_URI = os.getenv("MONGODB_URI")
        DB_NAME = os.getenv("DB_NAME")

        if not MONGODB_URI or not DB_NAME:
            raise ValueError("MONGODB_URI and DB_NAME environment variables are required.")
            
        return MONGODB_URI, DB_NAME
    
    except Exception as e:
        print(f"Error loading environment variables: \n{e}")
        raise e



def initMongoClient():
    try:
        MONGODB_URI, DB_NAME = load_credentials()
        client = MongoClient(MONGODB_URI)
        print("MongoDB connection: Successful")
        db = client[DB_NAME]
        return db
    
    except ConnectionFailure as e:
        print(f"MongoDB connection: Failed\n{e}")
        raise e
    except Exception as e:
        print(f"MongoDB initialization error: {e}")
        raise e
    

def main():
    db = initMongoClient()
    print("Database initialized:", db.name)

    users_collection = db["users"]
    return users_collection


try:
    db = initMongoClient()
    users_collection = db["users"]
except Exception as e:
    print(f"Failed to initialize database: {e}")
    raise e