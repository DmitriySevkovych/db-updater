import os
from dotenv import load_dotenv

import logging
from pathlib import Path
# from db.reader import *
from db.reader_homedb import *

if __name__ == "__main__":

    load_dotenv()

    db_file = os.getenv("DB_FILE")

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)

    # Reader().query(db_file, "SELECT * FROM ref_blueprint")
    HomeDBReader().getBlueprints()

    print('end')
