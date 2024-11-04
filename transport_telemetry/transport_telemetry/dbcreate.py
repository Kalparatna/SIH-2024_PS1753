import mysql.connector
from mysql.connector import Error

def create_database(db_name):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Kalparatna@2023'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database '{db_name}' created successfully.")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Specify the database name
database_name = 'transport'
create_database(database_name)
