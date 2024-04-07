import sqlite3

with sqlite3.connect("db.sqlite3") as db:
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE Department(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL);''')
