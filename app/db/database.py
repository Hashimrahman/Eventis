import os

from dotenv import load_dotenv
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


def get_user_collection():
    return db["users"]
