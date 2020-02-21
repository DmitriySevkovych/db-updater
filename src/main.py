import os
from dotenv import load_dotenv

import logging
from pathlib import Path

from db.reader_homedb import *
from db.writer_homedb import *


if __name__ == "__main__":

    load_dotenv()

    db_file = os.getenv("DB_FILE")

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)

    blueprints = HomeDBReader().getBlueprints()

    for blueprint in blueprints:
        print(f"""INSERT INTO expenses{blueprint.getExpenseAttributes()} VALUES {blueprint.getExpensePlaceholders()}""")
        print(blueprint.getExpenseValues())
        break

    print('end')
