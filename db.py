import sqlite3
from sqlite3 import Error
import pandas as pd

#_cursor = conn.cursor()
#_cursor.execute('CREATE TABLE test (id, Book Name text, Author text, Genre text, Sub-category text, Status text, Summary text)')

# Below commented code is used to initialize the database, create table in the database
# and to populate database using excel file. 
# Note the for loop is used to remove the space from the column headers as they were causing error while fetching data
# from the database. If your column header doesnot contain white space between headers, you can skip that for loop
# and the df.columns part
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
            print("create_connection failed")


def get_all_itens(loc):
    try:
        conn = create_connection(loc = r'D:\sqlite\db\books.db')
        _cursor = conn.cursor()
        _cursor.execute("Select * from books")
        rows = _cursor.fetchall()
        return {"count": len(rows), "items": rows}
    except Error as e:
        print('Error: ', e)
        return None
    finally:
        if conn:
            conn.close()
        else:
            print("get_all_items failed")


def get_completed(loc = r'D:\sqlite\db\books.db'):
    try:
        conn = create_connection(loc)
        _cursor = conn.cursor()
        _cursor.execute("Select * from Books where status = 'C'")
        rows = _cursor.fetchall()
        return rows
    except Error as e:
        print('Error: ', e)
        return None
    finally:
        if conn:
            conn.close()
        else:
            print("get_completed failed")

def get_reading(loc = r'D:\sqlite\db\books.db'):
    try:
        conn = create_connection(loc)
        _cursor = conn.cursor()
        _cursor.execute("Select * from Books where status = 'R'")
        rows = _cursor.fetchall()
        conn.close()
        return rows
    except Error as e:
        print('Error: ', e)
        return None
    finally:
        if conn:
            conn.close()
        else:
            print("get_reading failed")

def get_want_to_read(loc = r'D:\sqlite\db\books.db'):
    try:
        conn = create_connection(loc)
        _cursor = conn.cursor()
        _cursor.execute("Select * from Books where status = 'F'")
        rows = _cursor.fetchall()
        conn.close()
        return rows
    except Error as e:
        print('Error: ', e)
        return None
    finally:
        if conn:
            conn.close()
        else:
            print("get_want_to_read failed")


def genre():
    try:
        conn = create_connection(r'D:\sqlite\db\books.db')
        _cursor = conn.cursor()
    except Error as e:
        print("Error: ", e)
        return None

    def get_fiction():
        pass