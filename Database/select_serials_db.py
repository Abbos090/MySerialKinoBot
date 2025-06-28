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


def select_serials():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select serial_name from serials;")

    rows = cur.fetchall()

    conn.commit()

    cur.close()
    conn.close()

    return rows