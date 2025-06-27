import psycopg2

def delete_serials_db(serial_id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()

    cur.execute("DELETE FROM serials WHERE serial_id = %s", (serial_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    conn.commit()
    cur.close()
    conn.close()

    return deleted


def delete_serial_qism_db(qism_id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()

    cur.execute("DELETE FROM serial WHERE serial_id = %s", (qism_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    conn.commit()
    cur.close()
    conn.close()

    return deleted

def delete_kino_db(kino_id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()

    cur.execute("DELETE FROM kinolar WHERE id = %s", (kino_id,))
    deleted = cur.rowcount  # o'chirilgan qatorlar soni

    conn.commit()
    cur.close()
    conn.close()

    return deleted