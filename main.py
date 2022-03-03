from os import getenv
from sys import argv
import sys
from db.crud.temp_crud import TempCRUD
import db.db as database
from dotenv import load_dotenv
import argparse
import logging
from sqlalchemy_utils import database_exists
from fastapi.encoders import jsonable_encoder
from api.api import app
from uvicorn.main import run

load_dotenv()
log = logging.getLogger(__name__)


def run_app():

    run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None,
    )


def main():

    parser = argparse.ArgumentParser(
        description="SQLite, SQLAlchemy and fast API backend."
    )
    parser.add_argument(
        "-r", "--run", action="store_true", help="run the backend"
    )
    parser.add_argument(
        "-m",
        "--migrate",
        action="store_true",
        help="create tables for database",
    )
    parser.add_argument(
        "-u",
        "--upgrade_revision",
        action="store_true",
        help="create migrate revision",
    )
    parser.add_argument(
        "-i", "--info", action="store_true", help="print out info logs"
    )
    parser.add_argument(
        "--message",
        required="--argument" in sys.argv,
        help="add message to revision",
    )

    args = parser.parse_args()

    if args.info:
        logging.basicConfig(level=logging.INFO)
        args.info = False

    if True not in vars(args).values():

        log.error("ERROR: At least one flag is required (--info not included)")
        parser.print_help()

    db_url = getenv("DB_URL")

    if args.run:
        engine = database.init_db(db_url)

        if not database_exists(engine.url):
            log.error("Database not created yet, run with -m, --migrate")
            parser.print_help()
            sys.exit(1)
        run_app()

    if args.migrate:
        database.migrate_tables(db_url)

    if args.upgrade_revision:
        message = ""
        if args.message:
            message = args.message

        database.create_migration(db_url, message)


if __name__ == "__main__":

    main()
