import os
from db.reader import Reader
from db.model import *

class HomeDBReader(Reader):
    def getBlueprints(self, ofType: str = None):
        db_file = os.getenv("DB_FILE")
        sql = """SELECT 
                    key
                    , type as blueprint_type
                    , frequency
                    , due_date
                    , due_weekday
                    , amount
                    , origin
                    , description
                    , source_bank_account
                    , target_bank_account
                    , tax_relevance
                    , tax_category
                FROM ref_blueprint"""
        
        if(ofType):
            sql += f" WHERE blueprint_type = '{ofType}'"

        blueprints = []

        rows = Reader().query(db_file, sql)

        for row in rows:
            (key, blueprint_type, frequency, due_date, due_weekday, amount, origin, description, source_account, target_account, tax_relevance, tax_category) = row
            blueprint = Blueprint(key,blueprint_type,frequency,due_date,due_weekday,amount,origin, description,source_account,target_account,tax_relevance,tax_category)
            blueprints.append(blueprint)
            print(blueprint)
        return blueprints