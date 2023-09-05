import sqlite3
import os
import csv


# Function to determine the data type of a value
def get_data_type(value):
    try:
        int(value)
        return "INTEGER"
    except ValueError:
        try:
            float(value)
            return "REAL"
        except ValueError:
            return "TEXT"


# Connect to the SQLite database
conn = sqlite3.connect("items.db")
cursor = conn.cursor()

# Get a list of CSV files in the "data" directory
data_dir = "data"  # Change this to your data directory path
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

# Iterate through CSV files and create tables
for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[
        0
    ]  # Remove the file extension to get the table name

    # Read the first row of the CSV file to determine the column names and data types
    with open(os.path.join(data_dir, csv_file), newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

    data_types = [get_data_type(value) for value in header]

    # Generate the CREATE TABLE statement dynamically based on the column names and data types
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
    for column_name, data_type in zip(header, data_types):
        create_table_sql += f"    {column_name} {data_type},\n"
    create_table_sql = create_table_sql.rstrip(",\n") + "\n);"

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_sql)

# Commit the changes and close the connection
conn.commit()
conn.close()
