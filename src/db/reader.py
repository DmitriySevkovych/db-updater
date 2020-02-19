from db.dbutils import create_connection


def query(db_file: str, sql: str):
    conn = create_connection(db_file)

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)
