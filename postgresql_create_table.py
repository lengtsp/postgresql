import psycopg2

# ข้อมูลการเชื่อมต่อ
DB_HOST = 'localhost'
DB_NAME = 'threads'  # ชื่อฐานข้อมูลเริ่มต้นของ PostgreSQL
DB_USER = 'postgres'
DB_PASS = 'threads'
DB_PORT = 5432

# สร้างตาราง student
def create_student_table():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS student (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            subject VARCHAR(255) NOT NULL,
            grade VARCHAR(5)
        );
        """
        cur.execute(create_table_query)

        # ข้อมูลตัวอย่างนักเรียนไทย 10 คน
        student_data = [
            ('สมชาย', 'สุขใจ', 'คณิตศาสตร์', 'A'),
            ('สมหญิง', 'ใจดี', 'วิทยาศาสตร์', 'B+'),
            ('สมศักดิ์', 'ใจสู้', 'ภาษาไทย', 'A-'),
            ('สมพร', 'ใจเย็น', 'สังคมศึกษา', 'B'),
            ('สมหมาย', 'ใจบุญ', 'ภาษาอังกฤษ', 'C+'),
            ('สมปอง', 'ใจเด็ด', 'ศิลปะ', 'A'),
            ('สมจิตร', 'ใจกล้า', 'ดนตรี', 'B-'),
            ('สมหวัง', 'ใจดี', 'สุขศึกษา', 'A+'),
            ('สมบูรณ์', 'ใจมั่น', 'พลศึกษา', 'C'),
            ('สมทรง', 'ใจงาม', 'คอมพิวเตอร์', 'B+')
        ]

        insert_query = """
        INSERT INTO student (first_name, last_name, subject, grade)
        VALUES (%s, %s, %s, %s);
        """
        cur.executemany(insert_query, student_data)

        conn.commit()
        print("สร้างตาราง student และเพิ่มข้อมูลตัวอย่างเรียบร้อยแล้ว")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"เกิดข้อผิดพลาด: {error}")
    finally:
        if conn is not None:
            cur.close()
            conn.close()

if __name__ == '__main__':
    create_student_table()