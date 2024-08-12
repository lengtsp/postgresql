# pip install psycopg2-binary
import psycopg2
try:
    print('try')
    # Connect to your postgres DB
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="pg_database",
        user="admin",
        password="admin_passw0rd"
    )

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Retrieve query results
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    print('ผ่าน')

except Exception as error:
    print('except')
    print("Error while connecting to PostgreSQL", error)
    print('ไม่ผ่าน')
    
finally:
    # Close the database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")




