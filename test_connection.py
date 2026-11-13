import mysql.connector
from mysql.connector import Error
import database
try:
    connection = database.get_connection()

    if connection.is_connected():
        print("Successfully connected!")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player")
        
        records = cursor.fetchall()
        for row in records:
            print(row)

except Error as e:
    print(f"Error connecting to MySQL: {e}")
finally: 
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()