
def row_exists(conn, table, id):
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM {} WHERE id = %s', (id,))
    row = cursor.fetchone()
    if row:
        return True
    else:
        return False
