import logging
import datetime

from db.model import *
from utils.datecheck import *


def schedule_transactions(blueprint: Blueprint) -> list:
    # Determine which days since the last update were paydays for the current blueprint
    schedule = []

    today = datetime.datetime.now().date()
    if(blueprint.last_update):
        days_passed = today - get_date_from_str(blueprint.last_update)
        delta = days_passed.days
    else:
        delta = 1
        logging.warn(f'The blueprint {blueprint} was never updated before!')

    logging.info(f'Scheduler will have to check the last {delta} days.')

    dates_to_check = [
        today - datetime.timedelta(days=x) for x in range(delta)]

    for check_date in dates_to_check:
        if(is_payment_due(check_date, blueprint)):
            transaction_date = get_next_transaction_date(check_date)
            schedule.append(Transaction(transaction_date, blueprint))
            logging.debug(
                f'Payment for {blueprint.key} is due on {check_date} and scheduled for {transaction_date}')

    logging.info(
        f'Scheduled {len(schedule)} transactions for blueprint {blueprint}')
    return schedule
