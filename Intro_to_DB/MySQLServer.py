import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'alx_book_store'

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{DB_NAME}' already exists.")
        else:
            print(f"Failed creating database: {err}")
            raise


def main():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1')
        cursor = cnx.cursor()
        try:
            create_database(cursor)
        finally:
            cursor.close()
            cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    main()
