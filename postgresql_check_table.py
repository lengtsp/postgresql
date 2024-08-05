import psycopg2

# ข้อมูลการเชื่อมต่อ
hostname = 'localhost'  # หรือ IP ของ Docker container หากต่างจาก localhost
port = 5432
username = 'postgres'
password = 'threads'
database = 'threads'

# เชื่อมต่อกับ PostgreSQL
try:
    connection = psycopg2.connect(
        host=hostname,
        port=port,
        user=username,
        password=password,
        dbname=database
    )

    cursor = connection.cursor()

    # คำสั่ง SQL เพื่อดึงชื่อตารางทั้งหมด
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)

    # ดึงข้อมูลทั้งหมดจากผลลัพธ์
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

except Exception as e:
    print("Error connecting to the database:", e)

finally:
    if connection:
        cursor.close()
        connection.close()