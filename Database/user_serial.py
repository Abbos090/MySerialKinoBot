import psycopg2

def get_serial_fasl(serial_name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT serial_fasl FROM serial WHERE serial_name = %s", (serial_name,))
    fasllar = [row[0] for row in cur.fetchall()]
    conn.close()
    return fasllar

def get_serial_all(serial_name, serial_fasl):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM serial WHERE serial_name = %s AND serial_fasl = %s ORDER BY serial_qism",
        (serial_name, serial_fasl)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
