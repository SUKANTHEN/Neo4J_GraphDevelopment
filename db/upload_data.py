"""
db/upload_data.py
-----------------

"""
import logging
import psycopg2
from db.config import DATABASE_NAME, USER_NAME, PASSWORD, HOST, PORT, SQL_FILE_PATH_1,SQL_FILE_PATH_2

def execute_sql_from_file(sql_file_path: str):
    """
    Function to `Execute SQL commands from a file`.

    Args:
    sql_file_path(str): Path to the SQL file to execute.
    """
    try:
        # Establish a database connection
        connection = psycopg2.connect(
            database=DATABASE_NAME,
            user=USER_NAME,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )

        cursor = connection.cursor()
        # Read and execute SQL commands from the SQL file
        with open(sql_file_path, 'r') as sql_file:
            sql_commands = sql_file.read()

        cursor.execute(sql_commands)
        # Commit the transaction
        connection.commit()
        logging.info("SQL query executed successfully!!")
        cursor.close()
        connection.close()
    except Exception as error:
        logging.error(f"Error: {error}")
        raise error



if __name__ == "__main__":
    try:
        execute_sql_from_file(SQL_FILE_PATH_2)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
