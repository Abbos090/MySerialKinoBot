import psycopg2
def create_serial_db(data):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")

    cur = conn.cursor()

    query = "INSERT INTO serials (serial_id, serial_name, serial_language, serial_janr, serial_year) VALUES (%s, %s, %s, %s, %s);"
    values = (data['serial_id'], data['serial_name'], data['serial_language'], data['serial_janr'], data['serial_year'])

    cur.execute(query, values)

    conn.commit()

    cur.close()
    conn.close()