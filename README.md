# Database Tooling for Managing SQLite Databases

This set of Python scripts and tools allows you to create and manage SQLite databases for storing and manipulating data from CSV files. It is designed to help you easily import data from CSV files into SQLite tables and set up the database schema. 

## Prerequisites

Before using these tools, ensure that you have Python installed on your system. You'll also need to have the required CSV files that you want to import into the database.

## Getting Started

1. **Clone the Repository**: Start by cloning this repository to your local machine or download the provided scripts.

2. **Modify Script Variables**:
   - Open the `main.py` script and update the paths and variables according to your specific use case:
     - `create_tables_script`: Set the path to your `createTables.py` script.
     - `import_data_script`: Set the path to your `importData.py` script.
   
   - Open the `createTables.py` script and define the database schema for your tables.
   - Update the CSV file names and paths in the `importData.py` script to match your data files.

3. **Run the Main Script**:
   - Execute the `main.py` script using the following command:
     ```bash
     python main.py
     ```
   - The script will first create the tables based on the schema defined in `createTables.py`.
   - It will then import data from your CSV files into the respective tables.
   - If any errors occur during these processes, they will be displayed in the console.

4. **Database Management**:
   - You can further customize the database schema and scripts to meet your specific needs.
   - The provided scripts handle resetting ID sequences and deleting existing data, so be cautious when using them on production databases.

## Database Structure

The database created by these scripts contains two tables: `reloading` and `ammo`. The schema for these tables can be customized in the `createTables.py` script.

## Customization

You can customize the following aspects of this tooling:

- Database schema in `createTables.py`.
- CSV file names and paths in `importData.py`.
- Starting ID values for each table.
- CSV data loading logic in `load_csv_data` function.

## Troubleshooting

If you encounter any issues or errors while using this tooling, please refer to the error messages displayed in the console for guidance.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed for your projects.

---

Happy database management!
