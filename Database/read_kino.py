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

def read_kino_db(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM kinolar WHERE id = %s", (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
            'id': row[0],
            'name': row[1],
            'language': row[2],
            'year': row[3],
            'janr': row[4],
            'qism': row[5],
            'second': row[6],
            'video_id': row[7]
        }
    return None

def read_kino_name_db(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM kinolar WHERE name = %s", (name,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return {
            'id': row[0],
            'name': row[1],
            'language': row[2],
            'year': row[3],
            'janr': row[4],
            'qism': row[5],
            'second': row[6],
            'video_id': row[7]
        }
    return None