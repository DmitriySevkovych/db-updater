import os
from datetime import date
from db.writer import Writer
from db.model import *

class HomeDBWriter(Writer):
    def write_expenses(self, blueprint: Blueprint):
        db_file = os.getenv("DB_FILE")
        sqlInsert = f"INSERT INTO expenses {self._get_expense_attributes()} VALUES {self._get_expense_placeholders()}"
        sqlUpdate = f"UPDATE ref_blueprint SET last_update='{date.today()}' WHERE key = ?"

        Writer().execute(db_file,sqlInsert,_get_expense_values(blueprint))
        Writer().execute(db_file,sqlUpdate,(blueprint.key,))

    def write_income(self):
        pass

    # Private helper functions
    def _get_expense_attributes(self) -> str:
        return "(date, type, price, origin, description, payment_source, tax_relevance, tax_category, agent)"

    def _get_expense_placeholders(self) -> str:
        return "(?, ?, ?, ?, ?, ?, ?, ?, ?)"

    def _get_expense_values(self,blueprint:Blueprint) -> tuple:
        return tuple([ 
            '#TODO: date'
            , self.transaction_type
            , self.amount
            , self.origin
            , self.description
            , self.source_bank_account
            , self.tax_relevance
            , self.tax_category
            , os.getenv('AGENT')
            ])

    def get_income_attributes(self):
        return ""

    def get_income_placeholders(self):
        return ""

    def get_income_values(self):
        return ""