import mysql.connector


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bright101"
    )
    
    if connection.is_connected():
        my_cursor = connection.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as err:
    print(f"Encounted error while creating database {err}")

finally:
    if connection.is_connected():
        connection.close()
        my_cursor.close()
        print("MYSQL is successfully closed.")