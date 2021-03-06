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
        print("Connection Successful")
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Function Executed Successfully")
        else:
            print("Unable to Connect")

conn = create_connection(r'D:\sqlite\db\test.db')
df = pd.read_excel('Booklist.xlsx', header=0, index_col=0)
print(df.head())
#conn.cursor().execute("DROP table 'Test Table'")
new_cols = []
for column in df.columns:
    cols = "".join(column.split())
    new_cols.append(cols)

print(new_cols)
df.columns = new_cols
print(df.head())

df.to_sql(name='Test Table', con = conn, if_exists='append') 
#('fail'- Default', 'replace'- To drop and create new)
