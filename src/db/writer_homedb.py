import os
from db.writer import Writer
from db.model import *

class HomeDBWriter(Writer):
    def writeExpenses(self, blueprint: Blueprint):
        db_file = os.getenv("DB_FILE")
        sql = f"""INSERT INTO expenses {blueprint.getExpenseAttributes()} VALUES {blueprint.getExpensePlaceholders()}"""

        Writer().insert(db_file,sql,blueprint.getExpenseValues())

    def writeIncome(self):
        pass