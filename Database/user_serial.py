import os
from urllib.parse import urlparse
import psycopg2

def get_connection():
    db_url = os.getenv("DATABASE_URL")
    result = urlparse(db_url)

    return psycopg2.connect(
        database=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )


def get_serial_fasl(serial_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT serial_fasl FROM serial WHERE serial_name = %s", (serial_name,))
    fasllar = [row[0] for row in cur.fetchall()]
    conn.close()
    return fasllar

def get_serial_all(serial_name, serial_fasl):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM serial WHERE serial_name = %s AND serial_fasl = %s ORDER BY serial_qism",
        (serial_name, serial_fasl)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
