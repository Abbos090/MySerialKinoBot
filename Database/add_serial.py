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

def add_serial_db(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"insert into serial (serial_id, serial_name, serial_language, serial_janr, serial_fasl, serial_year, qism_id, serial_qism, video_id, second)"
                f"values ({data['serial_info']['serial_id']}, '{data['serial_info']['serial_name']}', '{data['serial_info']['serial_language']}', '{data['serial_info']['serial_janr']}', {data['serial_fasl']}, {data['serial_info']['serial_year']}, {data['qism_id']}, {data['serial_qism']}, '{data['video_id']}', {data['second']});")

    conn.commit()

    cur.close()
    conn.close()


