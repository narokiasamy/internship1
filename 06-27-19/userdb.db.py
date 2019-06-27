import sqlite3

con = sqlite3.connect("userdb.db")
cursorObj = con.cursor()