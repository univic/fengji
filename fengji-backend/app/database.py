import pymongo
from app import app_config


def create_db_connection():
    db = pymongo.MongoClient(app_config.MONGODB_SETTINGS["host"])
    return db


fengji_db = create_db_connection()
