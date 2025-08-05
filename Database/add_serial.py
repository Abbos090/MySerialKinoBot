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

    # Oralig‘larni aniqlaymiz
    qism_ids = list(range(int(data['qism_ids'][0]), int(data['qism_ids'][1]) + 1))
    serial_qisms = list(range(int(data['serial_qisms'][0]), int(data['serial_qisms'][1]) + 1))

    videos = data['videos']        # file_id lar
    seconds = data['seconds']      # duration lar

    # Himoya: uzunliklar teng bo‘lishi kerak
    if not (len(videos) == len(seconds) == len(qism_ids) == len(serial_qisms)):
        raise ValueError("Ma'lumotlar soni bir-biriga mos emas!")

    for i in range(len(videos)):
        cur.execute(
            """
            INSERT INTO serial (
                serial_id, serial_name, serial_language, serial_janr,
                serial_fasl, serial_year, qism_id, serial_qism, video_id, second
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                data['serial_info']['serial_id'],
                data['serial_info']['serial_name'],
                data['serial_info']['serial_language'],
                data['serial_info']['serial_janr'],
                data['serial_fasl'],
                data['serial_info']['serial_year'],
                qism_ids[i],
                serial_qisms[i],
                videos[i],
                seconds[i]
            )
        )

    conn.commit()
    cur.close()
    conn.close()
