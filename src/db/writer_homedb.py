import os
from datetime import date
from db.writer import Writer
from db.model import *


class HomeDBWriter(Writer):
    def write_expenses(self, transaction: Transaction):
        db_file = os.getenv("DB_FILE")
        sqlInsert = f"INSERT INTO expenses {self._get_expense_attributes()} VALUES {self._get_expense_placeholders()}"
        sqlUpdate = f"UPDATE ref_blueprint SET last_update='{date.today()}' WHERE key = ?"

        writer = Writer()
        # writer.execute(db_file,sqlInsert,self._get_expense_values(transaction))
        writer.execute(db_file, sqlUpdate, (transaction.blueprint.key,))

    def write_income(self, transaction: Transaction):
        db_file = os.getenv("DB_FILE")
        sqlInsert = f"INSERT INTO income {self._get_income_attributes()} VALUES {self._get_income_placeholders()}"
        sqlUpdate = f"UPDATE ref_blueprint SET last_update='{date.today()}' WHERE key = ?"

        writer = Writer()
        # writer.execute(db_file,sqlInsert,self._get_income_values(transaction))
        writer.execute(db_file, sqlUpdate, (transaction.blueprint.key,))

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
