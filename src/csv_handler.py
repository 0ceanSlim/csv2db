import csv

class CSVHandler:
    def __init__(self, paths):
        self.paths = paths

    def load_to_db(self, db):
        for path in self.paths:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    db.insert(row)
        db.close()