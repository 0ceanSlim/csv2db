# CSV to Database (csv2db)

## Introduction

`csv2db`, is a simple Python tool that allows you to create a database from CSV files. This README.md provides step-by-step instructions on how to use `csv2db` to efficiently convert your CSV data into a SQLite database.

## Prerequisites

Before using these tools, ensure that you have the following prerequisites installed on your system:

- Python: You need Python installed to run the script.
- CSV Files: You should have the CSV files that you want to import into the database ready.

## Getting Started

To begin using `csv2db`, follow these steps:

1. Open a Terminal or Command Prompt and navigate to where you want to clone this repository

2. Clone this repository to your local machine using the following command:

    ```bash
    git clone https://git.happytavern.co/oceanslim/csv2db.git
    ```
   or
    ```bash
    git clone https://github.com/0ceanslim/csv2db.git
    ```

3. Place the CSV file(s) you want to convert into a database in the `data` folder within the project directory.  
*(there are some example CSV files already in this project. Remove them after adding your own)*

## Configuration (Optional)

If you want to customize the starting IDs for your table data entries, you can modify the `id.py` file before running the conversion. This step is entirely optional and can be skipped if you want to use the default IDs.

## Usage

1. Open your terminal or command prompt.

2. Navigate to the project directory where you cloned the repository.

3. Run the `main.py` script to initiate the CSV to database conversion process:

    ```bash
    python main.py
    ```

4. `csv2db` will process the CSV file(s) and create a corresponding SQLite database in the same directory as the project.

## Feedback and Contributions
I welcome feedback, bug reports, and contributions. Feel free to open an issue or submit a pull request on my GitHub or HappyTavern repository if you have any suggestions or improvements.