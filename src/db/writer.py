from db.dbutils import create_connection

class Writer:
    def insert(self: Writer, db_file: str, sql: str, params: tuple):
        conn = create_connection(db_file)
        cur = conn.cursor()

        cur.execute(sql, params)

        return cur.lastrowid

