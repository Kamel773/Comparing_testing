
import psycopg2

def vacuum_db(host, dbname, user, password):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("VACUUM")
    cur.close()
    conn.close()
