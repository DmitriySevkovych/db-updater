import logging
from datetime import date
from db.model import *


def is_payment_due(check_date: date, blueprint: Blueprint) -> bool:
    # TODO validate + log

    frequency = blueprint.frequency
    
    due_date = blueprint.due_date
    due_weekday = Weekday[blueprint.due_weekday] if blueprint.due_weekday else None
    
    last_update = blueprint.last_update

    if(frequency == 'WEEKLY'):
        return _is_weekly_payment_due(check_date, due_weekday)
    elif(frequency == 'MONTHLY'):
        pass
    elif(frequency == 'QUARTERLY'):
        pass
    elif(frequency == 'SEMI-ANNUALLY'):
        pass
    elif(frequency == 'ANNUALLY'):
        pass
    else:
        raise Exception()  # TODO log and parametrise exception


# Private helper methods

def _is_weekly_payment_due(check_date: date, due_weekday: Weekday) -> bool:

    if(due_weekday == None):
        logging.error(f'Encountered WEEKLY frequency, but blueprintdue_weekday is None!')
        raise Exception()

    check_weekday = Weekday(check_date.weekday())
    return due_weekday == check_weekday


def _is_monthly_payment_due(check_date: date, due_date: date):
    pass
