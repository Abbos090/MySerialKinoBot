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

def create_serial_db(data):
    conn = get_connection()
    cur = conn.cursor()

    query = "INSERT INTO serials (serial_id, serial_name, serial_language, serial_janr, serial_year) VALUES (%s, %s, %s, %s, %s);"
    values = (data['serial_id'], data['serial_name'], data['serial_language'], data['serial_janr'], data['serial_year'])

    cur.execute(query, values)

    conn.commit()

    cur.close()
    conn.close()