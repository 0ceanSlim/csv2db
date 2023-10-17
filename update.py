import sqlite3
import os
import csv

# starting_ids.py

starting_ids = {
    "table1": 1000,
    "table2": 2000,
    "table3": 3000,
}


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


# Connect to the SQLite database and delete existing tables
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Get a list of CSV files in the "data" directory
data_dir = "data"  # Change this to your data directory path
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

# Drop all existing tables except for sqlite_sequence
cursor.execute("PRAGMA foreign_keys = OFF;")
cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_sequence';"
)
existing_tables = cursor.fetchall()
for table in existing_tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")

# Commit the changes to delete existing tables
conn.commit()

# Iterate through CSV files and create new tables
for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[0]

    # Read the first row of the CSV file to determine the column names
    with open(os.path.join(data_dir, csv_file), newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

    # Read the second row to determine data types
    with open(os.path.join(data_dir, csv_file), newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        data_row = next(csv_reader)
        data_types = [get_data_type(value) for value in data_row]

    # Add a primary key column if needed (replace 'unique_id' with your unique identifier column name)
    if "unique_id" in header:
        header[header.index("unique_id")] += " PRIMARY KEY"

    # Generate the CREATE TABLE statement dynamically based on the column names and data types
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
    for column_name, data_type in zip(header, data_types):
        create_table_sql += f"    {column_name} {data_type},\n"
    create_table_sql = create_table_sql.rstrip(",\n") + "\n);"

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_sql)

    # Read and insert data from the CSV file into the table
    with open(os.path.join(data_dir, csv_file), newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            placeholders = ",".join(["?"] * len(row))
            insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders});"
            cursor.execute(insert_sql, row)

# Commit the changes and close the connection
conn.commit()
conn.close()


# Connect to the SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Define the directory where the CSV files are located
csv_directory = "data"  # Change this to your directory path


# Function to load data from a CSV file into a table
def load_csv_data(csv_path, table_name, cursor, starting_id):
    # Delete existing data in the table
    delete_query = f"DELETE FROM {table_name}"
    cursor.execute(delete_query)

    with open(csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row if it exists in the CSV
        for row in csv_reader:
            # Exclude the first column (id) from the row
            values = row[1:]
            placeholders = ", ".join(["?"] * len(values))
            insert_query = f"INSERT INTO {table_name} VALUES (?, {placeholders})"
            cursor.execute(insert_query, [starting_id] + values)
            starting_id += 1


# Get a list of CSV files in the data directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith(".csv")]

# Loop through the CSV files and load data into respective tables
for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[
        0
    ]  # Remove the file extension to get the table name
    csv_path = os.path.join(csv_directory, csv_file)
    if table_name in starting_ids:
        starting_id = starting_ids[table_name]
        load_csv_data(csv_path, table_name, cursor, starting_id)

# Commit the changes and close the connection
conn.commit()
conn.close()