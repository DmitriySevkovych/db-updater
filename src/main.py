import logging
from pathlib import Path
from db.reader import *

if __name__ == "__main__":


    db_file = r"/home/dmitriy/share/home/home.db"

    # Configure logging
    path = Path(db_file)
    logging.basicConfig(filename=f'{path.parent}/{path.stem}.log', level=logging.DEBUG)

    query(db_file, "SELECT * FROM expenses")

    print('end')
