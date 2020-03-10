from sqlite3 import *
import logging


def create_connection(db_file: str) -> Connection:

    # Initialize a connection object
    conn = None
    try:
        conn = connect(db_file)
        logging.debug(f'Connection to database {db_file}  initialized')
    except Error as e:
        logging.critical(f'Could not connect to database {db_file}')
        logging.debug(e)
        raise e

    return conn
