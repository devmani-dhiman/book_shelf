import sqlite3
from sqlite3 import Error
import pandas as pd

#_cursor = conn.cursor()
#_cursor.execute('CREATE TABLE test (id, Book Name text, Author text, Genre text, Sub-category text, Status text, Summary text)')


def create_connection(db_file):
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Function Executed Successfully")
            print(sqlite3.version)
        else:
            print("Unable to Connect")


def get_all_itens(loc):
    try:
        conn = create_connection(loc = r'D:\sqlite\db\books.db')
        _cursor = conn.cursor()
        _cursor.execute("Select * from books")
        rows = _cursor.fetchall()
        conn.close()
        return {"count": len(rows), "items": rows}
    except Error as e:
        print('Error: ', e)
        return None

def get_reading(loc = r'D:\sqlite\db\books.db'):
    try:
        conn = create_connection(loc)
        _cursor = conn.cursor()
        _cursor.execute("Select * from Books where status = 'C'")
        rows = _cursor.fetchall()
        return rows
        conn.close()
    except Error as e:
        print('Error: ', e)
        return None

def get_current():
    pass

"""
conn = create_connection(r'D:\sqlite\db\books.db')
df = pd.read_excel('Booklist.xlsx', header=0, index_col=0)
#print(df.head())
#conn.cursor().execute("DROP table 'Test Table'")
new_cols = []
for column in df.columns:
    cols = "".join(column.split())
    new_cols.append(cols)

#print(new_cols)
df.columns = new_cols
#print(df.head())

df.to_sql(name='Books', con = conn, if_exists='append') 
#('fail'- Default', 'replace'- To drop and create new)
conn.close()"""