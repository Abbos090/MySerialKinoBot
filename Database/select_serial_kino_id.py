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


def select_serial_id_db(serial_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT serial_name FROM serial WHERE qism_id = %s", (serial_id,))
        result = cur.fetchone()
        return result is not None  # True agar topilsa, aks holda False
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    finally:
        cur.close()
        conn.close()


def select_kino_id_db(kino_id):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='1221')
    cur = conn.cursor()

    try:
        cur.execute("SELECT name FROM kinolar WHERE id = %s", (kino_id,))
        result = cur.fetchone()
        return result is not None  # True agar topilsa, aks holda False
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    finally:
        cur.close()
        conn.close()
