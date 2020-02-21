
from dataclasses import dataclass
import datetime
import os

@dataclass
class Blueprint:
    key: str
    blueprint_type: str
    frequency: str
    due_date: datetime.date
    due_weekday: str
    transaction_type: str
    amount: float
    origin: str
    description: str
    source_bank_account: str
    target_bank_account: str
    tax_relevance: int
    tax_category: str


    def getExpenseAttributes(self):
        statement = """ (date, type, price, origin, description, payment_source, tax_relevance, tax_category, recorder) """
        return statement

    def getExpensePlaceholders(self):
        statement = """(?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        return statement

    def getExpenseValues(self):
        statement = tuple([ 
            '#TODO: date'
            , self.transaction_type
            , self.amount
            , self.origin
            , self.description
            , self.source_bank_account
            , self.tax_relevance
            , self.tax_category
            , os.getenv('RECORDER')
            ])

        return statement