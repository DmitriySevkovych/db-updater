from datetime import date
from db.model import *

def determine_payment_date(blueprint: Blueprint):
    today = date.today()
    today_weekday = Weekday(today.weekday())
    
    frequency = blueprint.frequency
    due_date = blueprint.due_date
    due_weekday = Weekday[blueprint.due_weekday]
    last_update = blueprint.last_update

    if( frequency == 'WEEKLY'):
        pass
