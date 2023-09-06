import tkinter as tk
from tkinter import filedialog
import subprocess

# Define the paths to your Python scripts
create_tables_script = "createTables.py"
import_data_script = "importData.py"

def create_database():
    """Creates the database based on the user input."""
    database_name = database_name_entry.get()
    data_directory = data_directory_entry.get()
    table_starting_ids = table_starting_ids_entry.get()

    # Check if the database name is empty
    if not database_name:
        tk.messagebox.showerror("Error", "Please enter a database name.")
        return

    # Check if the data directory is empty
    if not data_directory:
        tk.messagebox.showerror("Error", "Please select a data directory.")
        return

    # Create the database
    subprocess.run(["python", create_tables_script], check=True)

    # Import the data into the database
    subprocess.run(["python", import_data_script], check=True)

    # Show a messagebox to inform the user that the database has been created
    tk.messagebox.showinfo("Success", "Database created successfully.")
    
def browse_directory(entry_field):
    """Opens a file dialog and allows the user to select a directory."""
    directory = filedialog.askdirectory()
    entry_field.insert(0, directory)

# Create the main window
window = tk.Tk()
window.title("Create Database")

# Create the database name label and entry field
database_name_label = tk.Label(text="Database name:")
database_name_entry = tk.Entry(width=50)

# Create the data directory label and entry field
data_directory_label = tk.Label(text="Data directory:")
data_directory_entry = tk.Entry(width=50)
data_directory_button = tk.Button(text="Browse", command=lambda: browse_directory(data_directory_entry))

# Create the table starting IDs label and entry field
table_starting_ids_label = tk.Label(text="Table starting IDs (optional):")
table_starting_ids_entry = tk.Entry(width=50)

# Create the create database button
create_database_button = tk.Button(text="Create database", command=create_database)

# Layout the widgets
database_name_label.grid(row=0, column=0)
database_name_entry.grid(row=0, column=1)

data_directory_label.grid(row=1, column=0)
data_directory_entry.grid(row=1, column=1)
data_directory_button.grid(row=1, column=2)

table_starting_ids_label.grid(row=2, column=0)
table_starting_ids_entry.grid(row=2, column=1)

create_database_button.grid(row=3, column=0)

# Bind the enter key to the create database button
#window.bind("<Return>", create_database)

# Run the mainloop
window.mainloop()




