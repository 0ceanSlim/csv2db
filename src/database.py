import sqlite3

class Database:
    def __init__(self, name, starting_id):
        self.conn = sqlite3.connect(f'{name}.db')
        self.cursor = self.conn.cursor()
        self.id = starting_id

    def insert(self, data):
        self.cursor.execute('INSERT INTO table VALUES (?, ?)', (self.id, data))
        self.id += 1
        self.conn.commit()

    def close(self):
        self.conn.close()