import subprocess

# Define the paths to your Python scripts
create_tables_script = "createTables.py"
import_data_script = "importData.py"

# Run the createTables.py script
try:
    subprocess.run(["python", create_tables_script], check=True)
    print("createTables.py script executed successfully.")
except subprocess.CalledProcessError:
    print("Error running createTables.py script.")
    exit(1)

# Run the importData.py script
try:
    subprocess.run(["python", import_data_script], check=True)
    print("importData.py script executed successfully.")
except subprocess.CalledProcessError:
    print("Error running importData.py script.")
    exit(1)
