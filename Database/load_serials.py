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


def load_serials_db(serial_name):
    conn = get_connection()
    cur = conn.cursor()

    # SQL Injection xavfsizligi uchun parametrli query ishlatilmoqda
    cur.execute("SELECT * FROM serials WHERE serial_name = %s", (serial_name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    # Agar natija mavjud bo‘lsa, birinchi qatordagi ma’lumotlarni qaytaradi
    if rows:
        row = rows[0]
        return {
            'serial_id': row[0],
            'serial_name': row[1],
            'serial_language': row[2],
            'serial_janr': row[3],
            'serial_year': row[4]
        }

    # Agar hech qanday natija topilmasa
    return None

