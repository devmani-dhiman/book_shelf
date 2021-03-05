import sqlite3

con = sqlite3.connect("books.db")

_cursor = con.cursor()

_cursor.execute('''CREATE TABLE books 
                            (id, book name text, author text, category text, summary text, status text)''')
