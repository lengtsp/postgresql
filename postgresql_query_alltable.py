import psycopg2

# ข้อมูลการเชื่อมต่อ (เหมือนเดิมจากสคริปต์ก่อนหน้า)
DB_HOST = 'localhost'
DB_NAME = 'threads'
DB_USER = 'postgres'
DB_PASS = 'threads'
DB_PORT = 5432

def query_student_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cur = conn.cursor()

        query = "SELECT * FROM student;"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)  # หรือแสดงผลในรูปแบบอื่นๆ ตามต้องการ

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"เกิดข้อผิดพลาด: {error}")
    finally:
        if conn is not None:
            cur.close()
            conn.close()

if __name__ == '__main__':
    query_student_data()