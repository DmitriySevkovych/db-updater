from db.dbutils import create_connection

class Reader:
    def query(self, db_file: str, sql: str) -> list:
        conn = create_connection(db_file)

        cur = conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        return rows