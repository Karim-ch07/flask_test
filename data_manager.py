import os
import mysql.connector
import time


DB_HOST = "ip-172-31-94-34"
DB_USER = "root"
DB_PASSWORD = "Lala-2023"
DB_NAME = "flightdb"
DB_PORT = "3306"

# Establish the database connection
def establish_db_connection():
    try:
        # Attempt to establish the MySQL database connection
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )

        # If successful, return the connection object
        return db

    except mysql.connector.Error as e:
        # Handle the error if connection establishment fails
        handle_failure()
        return None

def handle_failure():
    print("Failed to establish a connection to the database.")

class DataManager:
    def __init__(self):
        self.dest_info = []
        self.cx_info = []
        self.db = establish_db_connection()

    def get_dest_info(self):
        # Retrieve data from the MySQL database
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM prices")
        self.dest_info = cursor.fetchall()
        cursor.close()
        return self.dest_info

    def update_dest_info_iata(self):
        # Update data in the MySQL database
        cursor = self.db.cursor()
        for dest in self.dest_info:
            sql = "UPDATE prices SET IATA = %s WHERE id = %s"
            val = (dest[2], dest[0])
            cursor.execute(sql, val)
            self.db.commit()
        cursor.close()

    # def get_cx_info(self):
    #     # Retrieve data from the MySQL database
    #     cursor = db.cursor()
    #     cursor.execute("SELECT * FROM users")
    #     self.cx_info = cursor.fetchall()
    #     cursor.close()
    #     return self.cx_info


# data_manager = DataManager()
# response = data_manager.get_dest_info()
# print(response)