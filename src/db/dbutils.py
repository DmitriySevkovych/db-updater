from sqlite3 import Connection, connect, Error
import logging


def create_connection(db_file: str) -> Connection:

    # Initialize a connection object
    conn = None
    try:
        conn = connect(db_file)
        logging.debug('Connection to database %s initialized', db_file)
    except Error as e:
        logging.critical('Could not connect to database %s', db_file)
        logging.debug(e)
        raise e

    return conn
