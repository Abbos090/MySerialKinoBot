import psycopg2

def select_kinolar_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()

    cur.execute("SELECT name FROM kinolar")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]
