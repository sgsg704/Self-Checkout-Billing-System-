import csv
import sqlite3
conn=sqlite3.connect('database.sqlite')
cur=conn.cursor()
cur.execute(
'''
CREATE TABLE USER(
Name varchar(20) NOT NULL,
Email vachar(30) NOT NULL UNIQUE,
Password varchar(30)
);
''')
#def invalid():

fname='customer.csv'
with open(fname, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name=row[0]
        email=row[1]
        password=row[2]

        cur.execute('''
        INSERT INTO USER VALUES(?,?,?)
        ''',(name,email,password))

        conn.commit()
