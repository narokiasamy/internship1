import sqlite3

con = sqlite3.connect("mydatabse.db")
cursorObj = con.cursor()

entities1 = (1, 'Natalie', 20000, 'IT', 'intern', '2019-06-27')
entities2 = (2, 'Niyanth', 20000, 'IT', 'intern', '2019-06-27')
entities3 = (3, 'Shashank', 20000, 'IT', 'intern', '2019-06-27')


cursorObj.execute(
    'INSERT INTO employees (id, name, salary, deparmtent, position, hireDate) VALUES (?, ?, ?, ?, ?, ?)', entities1)
cursorObj.execute(
    'INSERT INTO employees (id, name, salary, deparmtent, position, hireDate) VALUES (?, ?, ?, ?, ?, ?)', entities2)
cursorObj.execute(
    'INSERT INTO employees (id, name, salary, deparmtent, position, hireDate) VALUES (?, ?, ?, ?, ?, ?)', entities3)
con.commit()

