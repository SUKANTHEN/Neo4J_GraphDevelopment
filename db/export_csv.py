import psycopg2
import csv
from db.config import DATABASE_NAME,USER_NAME,PASSWORD,HOST,PORT

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    database=DATABASE_NAME,
    user=USER_NAME,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

# Specify the SQL queries to select data for CSV files
query_employee = "SELECT * FROM employees"
query_department = "SELECT * FROM departments"

# Specify the CSV file paths
csv_file_path_employee = "db/employees.csv"
csv_file_path_department = "db/departments.csv"

cursor = connection.cursor()

cursor.execute(query_employee)
data_employee = cursor.fetchall()

cursor.execute(query_department)
data_department = cursor.fetchall()

# Write data to CSV files
with open(csv_file_path_employee, 'w', newline='') as csv_file_employee, open(csv_file_path_department, 'w', newline='') as csv_file_department:
    csv_writer_employee = csv.writer(csv_file_employee)
    csv_writer_department = csv.writer(csv_file_department)

    # Write column headers
    csv_writer_employee.writerow([desc[0] for desc in cursor.description])
    csv_writer_department.writerow([desc[0] for desc in cursor.description])

    # Write data to CSV files
    csv_writer_employee.writerows(data_employee)
    csv_writer_department.writerows(data_department)

# Close cursor and connection
cursor.close()
connection.close()
