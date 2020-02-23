import os
from dotenv import load_dotenv

import logging
from datetime import datetime
from pathlib import Path

from db.reader_homedb import *
from db.writer_homedb import *
from utils.scheduler import *


if __name__ == "__main__":

    load_dotenv()

    db_file = os.getenv("DB_FILE")

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(
        filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)
    logging.info(f'Working with database {db_file}')
    logging.debug('Start processing')

    home_db_reader = HomeDBReader()
    home_db_writer = HomeDBWriter()

    for blueprint in home_db_reader.get_blueprints('expense'):
        for transaction in schedule_transactions(blueprint):
            home_db_writer.write_expenses(transaction)
        home_db_writer.update_blueprint(blueprint)


    for blueprint in home_db_reader.get_blueprints('income'):
        for transaction in schedule_transactions(blueprint):
            HomeDBWriter().write_income(transaction)
        home_db_writer.update_blueprint(blueprint)

    logging.debug('End processing')
    print('end')
