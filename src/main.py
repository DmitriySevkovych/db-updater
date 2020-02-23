import os
from dotenv import load_dotenv

import logging
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
    for blueprint in home_db_reader.get_blueprints('expense'):
        logging.debug(f'Retrieved blueprint {blueprint} from the database')
        for transaction in schedule_transactions(blueprint):
            print(
                f'Expense transaction on {transaction.date}: {transaction.blueprint.key}')
            # HomeDBWriter().write_expenses(transaction)

    for blueprint in home_db_reader.get_blueprints('income'):
        logging.debug(f'Retrieved blueprint {blueprint} from the database')
        for transaction in schedule_transactions(blueprint):
            print(
                f'Income transaction on {transaction.date}: {transaction.blueprint.key}')
            # HomeDBWriter().write_income(transaction)

    logging.debug('End processing')
    print('end')
