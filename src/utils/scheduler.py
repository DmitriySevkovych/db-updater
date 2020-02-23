import datetime
from db.model import *
from utils.datecheck import *


def schedule_transactions(blueprint: Blueprint) -> list:
    # Determine which days since the last update were paydays for the current blueprint
    schedule = []

    today = datetime.datetime.now().date()
    yesterday = today - datetime.timedelta(days=1)
    last_update = datetime.datetime.strptime(blueprint.last_update, '%Y-%m-%d').date() if blueprint.last_update else yesterday
    delta = today - last_update

    dates_to_check = [
        today - datetime.timedelta(days=x) for x in range(delta.days)]

    for check_date in dates_to_check:
        if(is_payment_due(check_date, blueprint)):
            schedule.append(Transaction(date=check_date, blueprint=blueprint))

    return schedule
