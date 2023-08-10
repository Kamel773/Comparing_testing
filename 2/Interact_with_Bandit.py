
import sqlite3

def counter(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ?", (table_name,))
    count = cursor.fetchone()[0]
    conn.close()
    return count
