import csv
import os
import sqlite3
from id import starting_ids

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
