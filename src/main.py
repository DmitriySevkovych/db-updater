import os
import logging

from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from db.reader_homedb import HomeDBReader
from db.writer_homedb import HomeDBWriter
from utils.scheduler import schedule_transactions
from utils.mailing import send_summary


def synchronize_db():

    load_dotenv()

    db_file = os.getenv("DB_FILE")

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(
        filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)
    logging.info('DB-UPDATER LAUNCHED ON %s', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.debug('Working with database %s', db_file)
    logging.debug('Start processing')

    home_db_reader = HomeDBReader()
    home_db_writer = HomeDBWriter()

    # Sync expenses
    for blueprint in home_db_reader.get_blueprints('expense'):
        logging.info('Start working on the expense blueprint %s', blueprint.key)
        for transaction in schedule_transactions(blueprint):
            home_db_writer.write_expenses(transaction)
        home_db_writer.update_blueprint(blueprint)
        logging.debug('Blueprint %s done!', blueprint.key)

    # Sync income
    for blueprint in home_db_reader.get_blueprints('income'):
        logging.info('Start working on the income blueprint %s', blueprint.key)
        for transaction in schedule_transactions(blueprint):
            home_db_writer.write_income(transaction)
        home_db_writer.update_blueprint(blueprint)
        logging.debug('Blueprint %s done!', blueprint.key)

    # Send mail with synchronisation summary
    logging.info('Preparing to send an update summary to %s', os.getenv("EMAIL_RECEIVERS"))
    send_summary(home_db_writer.get_summary())
    logging.debug('Sending update summary done!')

    logging.debug('End processing')
    print('Database successfully updated')


if __name__ == "__main__":
    synchronize_db()
