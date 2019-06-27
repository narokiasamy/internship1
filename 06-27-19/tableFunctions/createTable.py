import sqlite3

con = sqlite3.connect("mydatabse.db")
cursorObj = con.cursor()

cursorObj.execute(
    "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, deparmtent text, position text, hireDate text)")
con.commit()
