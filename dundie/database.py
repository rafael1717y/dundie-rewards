import json

from dundie.settings import DATABASE_PATH

EMPTY_DB = {"people": {}, "balance": {}, "movement": {}, "users": {}}


def connect() -> dict:
    try:
        with open(DATABASE_PATH, "r") as database_file:
            return json.loads(database_file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return EMPTY_DB
