import logging
from datetime import date
from db.model import *


def is_payment_due(check_date: date, blueprint: Blueprint) -> bool:
    # TODO validate + log

    frequency = Frequency[blueprint.frequency]
    due_date = get_date_from_str(
        blueprint.due_date) if blueprint.due_date else None
    due_weekday = Weekday[blueprint.due_weekday] if blueprint.due_weekday else None

    if(frequency == Frequency.WEEKLY):
        return _is_weekly_payment_due(check_date, due_weekday)
    else:
        return _is_regular_payment_due(check_date, due_date, frequency)


def get_next_transaction_date(check_date) -> date:
    check_day = Weekday(check_date.weekday())

    if(check_day == Weekday.SATURDAY):
        return check_date + datetime.timedelta(days=2)
    elif(check_day == Weekday.SUNDAY):
        return check_date + datetime.timedelta(days=1)

    return check_date


def get_date_from_str(datestring: str) -> date:
    return datetime.datetime.strptime(datestring, '%Y-%m-%d').date()


# Private helper methods

def _is_weekly_payment_due(check_date: date, due_weekday: Weekday) -> bool:

    if(due_weekday == None):
        logging.error(
            f'Encountered WEEKLY frequency, but blueprintdue_weekday is None!')
        raise Exception()

    check_weekday = Weekday(check_date.weekday())
    return due_weekday == check_weekday


def _is_regular_payment_due(check_date: date, due_date: date, frequency: Frequency):
    delta = check_date.month - due_date.month + (check_date.year - due_date.year)*12
    return check_date.day == due_date.day and delta % frequency.value == 0
