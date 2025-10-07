import os
import mongomock


class DevConfig:

    MONGODB_SETTINGS = {
        "db": os.getenv("MONGODB_DB"),
        "host": os.getenv("MONGODB_HOST"),
        "username": os.getenv("MONGODB_USER"),
        "password": os.getenv("MONGODB_PASSWORD"),
    }


class MockConfig:

    MONGODB_SETTINGS = {
        "db": "users",
        "host": "mongodb://localhost",
        "mongo_client_class": mongomock.MongoClient,
    }


class ProdConfig:

    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")

    URI = (
        f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@"
        f"{MONGODB_HOST}/{MONGODB_DB}?authSource=users"
    )

    MONGODB_SETTINGS = {"host": URI}
