import psycopg2
def add_kino_db(data):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")

    cur = conn.cursor()

    cur.execute(f"insert into kinolar(id, name, language, year, janr, qism, second, video_id) values ({data['id']}, '{data['name']}', '{data['language']}', {data['year']}, '{data['janr']}', {data['qism']}, {data['second']}, '{data['video_id']}');")

    conn.commit()

    cur.close()
    conn.close()
