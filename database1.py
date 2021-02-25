import sqlite3

#CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT, analysis real)"
CREATE_TABLEs = '''CREATE TABLE IF NOT EXISTS entries
                    (content TEXT, date TEXT, analysis TEXT)'''


CREATE_ENTRYs = "INSERT INTO entries VALUES (?, ?, ?)"
RETRIEVE_ENTRIESs = "SELECT * FROM entries"


def create_table():
    with sqlite3.connect("data1.db") as connection:
        connection.execute(CREATE_TABLEs)


def create_entrys(content, date, analysis):
    with sqlite3.connect("data1.db") as connection:
        connection.execute(CREATE_ENTRYs, (content, date, analysis))


def retrieve_entrie():
    with sqlite3.connect("data1.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIESs)
        return cursor.fetchall()
