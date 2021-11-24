import sqlite3
conn=sqlite3.connect('test.db')
print("opened db")
conn.execute('CREATE TABLE CheckData (Amount TEXT,Name TEXT)')
print("table created")
conn.close()


