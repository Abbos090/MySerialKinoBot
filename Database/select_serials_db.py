import psycopg2

def select_serials():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")

    cur = conn.cursor()

    cur.execute("select serial_name from serials;")

    rows = cur.fetchall()

    conn.commit()

    cur.close()
    conn.close()

    return rows