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


def delete_serials_db(serial_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM serials WHERE serial_id = %s", (serial_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    cur.execute("DELETE FROM serial WHERE serial_id = %s", (serial_id,))

    conn.commit()
    cur.close()
    conn.close()

    return deleted


def delete_serial_qism_db(qism_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM serial WHERE serial_id = %s", (qism_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    conn.commit()
    cur.close()
    conn.close()

    return deleted

def delete_kino_db(kino_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM kinolar WHERE id = %s", (kino_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    conn.commit()
    cur.close()
    conn.close()

    return deleted