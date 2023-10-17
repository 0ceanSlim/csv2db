import tkinter as tk
from tkinter import filedialog
from database import Database
from csv_handler import CSVHandler

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.database_name = tk.StringVar()
        self.starting_id = tk.IntVar()
        self.csv_paths = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text='Database Name:').pack()
        tk.Entry(self.window, textvariable=self.database_name).pack()

        tk.Label(self.window, text='Starting ID:').pack()
        tk.Entry(self.window, textvariable=self.starting_id).pack()

        tk.Button(self.window, text='Select CSVs', command=self.select_csvs).pack()

        tk.Button(self.window, text='Create Database', command=self.create_database).pack()

    def select_csvs(self):
        self.csv_paths = filedialog.askopenfilenames(filetypes=[('CSV Files', '*.csv')])

    def create_database(self):
        db = Database(self.database_name.get(), self.starting_id.get())
        handler = CSVHandler(self.csv_paths)
        handler.load_to_db(db)

        self.window.destroy()

if __name__ == '__main__':
    GUI().window.mainloop()