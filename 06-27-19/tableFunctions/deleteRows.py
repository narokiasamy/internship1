import sqlite3

con = sqlite3.connect("mydatabse.db")
cursorObj = con.cursor()

cursorObj.execute('DELETE FROM employees')
con.commit()

