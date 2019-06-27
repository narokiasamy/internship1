import sqlite3

con = sqlite3.connect("mydatabse.db")
cursorObj = con.cursor()

cursorObj.execute('SELECT * FROM employees')
con.commit()

rows = cursorObj.fetchall()

for row in rows:
    print (row)