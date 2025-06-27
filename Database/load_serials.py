import psycopg2

def load_serials_db(serial_name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
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

