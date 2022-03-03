import sqlite3
import logging

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.orm.session import Session

from db.alembic.alembic_runner import run_alembic

log = logging.getLogger(__name__)


import logging


log = logging.getLogger(__name__)

ENGINE = None
SESSION_LOCAL: sessionmaker = None

Base = declarative_base()


def init_db(db_url: str) -> Engine:

    global Engine
    global SESSION_LOCAL
    global ENGINE
    log.info(f"DB-URL: {db_url}")
    ENGINE = create_engine(
        f"sqlite:///./{db_url}",
    )

    SESSION_LOCAL = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE,
    )

    log.info("INIT DB")
    return ENGINE


def get_db() -> Generator[Session, None, None]:

    global SESSION_LOCAL
    db = SESSION_LOCAL()
    try:
        yield db

    finally:

        db.rollback()
        db.close()


def migrate_tables(db_file):

    log.info("Migrating tables ... ")

    run_alembic(f"sqlite:///./{db_file}", ["upgrade", "head"])


def create_migration(db_file, message):

    conn = sqlite3.connect(db_file)
    log.info(f"SQLlite Version: {sqlite3.version}")
    conn.close()

    run_alembic(f"sqlite:///./{db_file}", ["revision", "--autogenerate", "-m", message])
