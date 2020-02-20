import os
from dotenv import load_dotenv

import logging
from pathlib import Path
from db.reader import *


if __name__ == "__main__":

    load_dotenv()

    db_file = os.getenv("DB_FILE")

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)

    query(db_file, "SELECT * FROM expenses")

    print('end')
