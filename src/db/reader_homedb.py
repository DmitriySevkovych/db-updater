import os
from db.reader import Reader
from db.model import *

class HomeDBReader(Reader):
    def get_blueprints(self, ofBlueprintType: str = None):
        db_file = os.getenv("DB_FILE")
        sql = """SELECT 
                    key
                    , blueprint_type
                    , frequency
                    , due_date
                    , due_weekday
                    , type as transaction_type
                    , amount
                    , origin
                    , description
                    , source_bank_account
                    , target_bank_account
                    , tax_relevance
                    , tax_category
                    , last_update
                FROM ref_blueprint"""
        
        if(ofBlueprintType):
            sql += f" WHERE blueprint_type = '{ofBlueprintType}'"

        blueprints = []

        rows = Reader().query(db_file, sql)

        for row in rows:
            (key, blueprint_type, frequency, due_date, due_weekday, transaction_type, amount, origin, description, source_account, target_account, tax_relevance, tax_category, last_update) = row
            blueprint = Blueprint(key,blueprint_type,frequency,due_date,due_weekday,transaction_type,amount,origin, description,source_account,target_account,tax_relevance,tax_category, last_update)
            blueprints.append(blueprint)
        return blueprints