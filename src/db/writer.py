from db.dbutils import create_connection


class Writer:
    def execute(self, db_file: str, sql: str, params: tuple):
        conn = create_connection(db_file)
        cur = conn.cursor()

        cur.execute(sql, params)

        conn.commit()

        return cur.lastrowid
