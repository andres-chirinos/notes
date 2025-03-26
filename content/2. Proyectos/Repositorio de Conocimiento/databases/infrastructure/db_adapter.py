# infrastructure/db_adapter.py
import sqlite3

class DBAdapter:
    def fetch_data(self, params):
        db_path = params["db_path"]
        query = params["query"]
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
