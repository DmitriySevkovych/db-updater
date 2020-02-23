from enum import Enum
from dataclasses import dataclass
import datetime


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class Frequency(Enum):
    WEEKLY = 0
    MONTHLY = 1
    QUARTERLY = 3
    SEMI_ANNUALLY = 6
    ANNUALLY = 12


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
    last_update: datetime.date


@dataclass
class Transaction:
    date: datetime.date
    blueprint: Blueprint
