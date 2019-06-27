import sqlite3

con = sqlite3.connect("mydatabse.db")
cursorObj = con.cursor()

cursorObj.execute('UPDATE employees SET name = "Natalie Arokiasamy" where id = 1')
con.commit()