from os import getenv
from db import DB
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    print(getenv("DB_URL"))
    DB.create_connection(getenv("DB_URL"))