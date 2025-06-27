import psycopg2
def add_serial_db(data):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")

    cur = conn.cursor()

    cur.execute(f"insert into serial (serial_id, serial_name, serial_language, serial_janr, serial_fasl, serial_year, qism_id, serial_qism, video_id, second)"
                f"values ({data['serial_info']['serial_id']}, '{data['serial_info']['serial_name']}', '{data['serial_info']['serial_language']}', '{data['serial_info']['serial_janr']}', {data['serial_fasl']}, {data['serial_info']['serial_year']}, {data['qism_id']}, {data['serial_qism']}, '{data['video_id']}', {data['second']});")

    conn.commit()

    cur.close()
    conn.close()


