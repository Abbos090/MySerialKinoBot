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

def add_kino_db(data):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO kinolar (id, name, language, year, janr, qism, second, video_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id'],
        data['name'],
        data['language'],
        data['year'],
        data['janr'],
        data['qism'],
        data['second'],
        data['video_id']
    )

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()
