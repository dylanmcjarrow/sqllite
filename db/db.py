import sqlite3
from sqlite3 import Error
import sys

class DB:
    
    def create_connection(db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
            sys.exit(0)
        finally:
            if conn:
                conn.close()
            
            
