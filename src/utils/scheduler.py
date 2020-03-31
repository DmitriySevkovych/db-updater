import logging
import datetime

from db.model import Blueprint, Transaction
from utils.datecheck import get_date_from_str, is_payment_due, get_next_transaction_date


def schedule_transactions(blueprint: Blueprint) -> list:
    # Determine which days since the last update were paydays for the current blueprint
    schedule = []

    today = datetime.datetime.now().date()
    if blueprint.last_update:
        days_passed = today - get_date_from_str(blueprint.last_update)
        delta = days_passed.days
    else:
        delta = 1
        logging.warning(
            'The blueprint %s was never updated before!', blueprint.key)

    logging.info('Scheduler will have to check the last %s days.', delta)

    dates_to_check = [
        today - datetime.timedelta(days=x) for x in range(delta)]

    for check_date in dates_to_check:
        if is_payment_due(check_date, blueprint):
            transaction_date = get_next_transaction_date(check_date)
            schedule.append(Transaction(transaction_date, blueprint))
            logging.debug('Payment for %s is due on %s and scheduled for %s',
                          blueprint.key, check_date, transaction_date)

    logging.info(
        'Scheduled %s transactions for blueprint %s', len(schedule), blueprint.key)
    return schedule
