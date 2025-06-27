import psycopg2

def read_kino_db(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
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
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
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