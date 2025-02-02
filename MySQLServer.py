import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='username',
        password='password'
    )

    # Check if connection is successful
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create alx_book_store database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        # Execute SQL query
        try:
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error:
            print(f"Error creating database")
        finally:
            # Close cursor
            cursor.close()

    else:
        print("Error connecting to MySQL server.")

except mysql.connector.Error:
    print(f"Error connecting to MySQL")

finally:
    # Close connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
