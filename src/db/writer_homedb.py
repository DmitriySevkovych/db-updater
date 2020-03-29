import os
from datetime import date
from collections import OrderedDict 

from db.writer import Writer
from db.model import *


class HomeDBWriter(Writer):

    def __init__(self):
        super().__init__()
        self.summary = {}


    def write_expenses(self, transaction: Transaction):
        db_file = os.getenv("DB_FILE")
        sqlInsert = f"INSERT INTO expenses {self._get_expense_attributes()} VALUES {self._get_expense_placeholders()}"

        Writer().execute(db_file, sqlInsert, self._get_expense_values(transaction))

        self._update_summary(transaction)


    def write_income(self, transaction: Transaction):
        db_file = os.getenv("DB_FILE")
        sqlInsert = f"INSERT INTO income {self._get_income_attributes()} VALUES {self._get_income_placeholders()}"

        Writer().execute(db_file, sqlInsert, self._get_income_values(transaction))

        self._update_summary(transaction)


    def update_blueprint(self, blueprint: Blueprint):
        db_file = os.getenv("DB_FILE")
        sqlUpdate = f"UPDATE blueprints SET last_update='{date.today()}' WHERE key = ?"

        Writer().execute(db_file, sqlUpdate, (blueprint.key,))


    def get_summary(self) -> OrderedDict:
        return OrderedDict( sorted( self.summary.items() ) )


    # Private helper functions

    def _get_expense_attributes(self) -> str:
        return "(date, type, price, origin, description, payment_source, tax_relevance, tax_category, agent)"


    def _get_expense_placeholders(self) -> str:
        return "(?, ?, ?, ?, ?, ?, ?, ?, ?)"


    def _get_expense_values(self, transaction: Transaction) -> tuple:

        blueprint = transaction.blueprint

        return tuple([
            transaction.date, blueprint.transaction_type, blueprint.amount, blueprint.origin, blueprint.description, blueprint.source_bank_account, blueprint.tax_relevance, blueprint.tax_category, os.getenv(
                'AGENT')
        ])


    def _get_income_attributes(self) -> str:
        return "(date, type, amount, origin, payment_to, agent)"


    def _get_income_placeholders(self) -> str:
        return "(?, ?, ?, ?, ?, ?)"


    def _get_income_values(self, transaction: Transaction) -> tuple:

        blueprint = transaction.blueprint

        return tuple([
            transaction.date, blueprint.transaction_type, blueprint.amount, blueprint.origin, blueprint.target_bank_account, os.getenv(
                'AGENT')
        ])


    def _update_summary(self, transaction: Transaction) -> None:
        transactions_on_date = self.summary.get(transaction.date, [])
        transactions_on_date.append(transaction.blueprint)
        self.summary[transaction.date] = transactions_on_date
