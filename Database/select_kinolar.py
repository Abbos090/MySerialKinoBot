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


def select_kinolar_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM kinolar")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]
