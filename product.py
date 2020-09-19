import csv
import sqlite3
conn=sqlite3.connect('database.sqlite')
cur=conn.cursor()
cur.execute('''
CREATE TABLE PRODUCT(
ID int(5) NOT NULL ,
Name vachar(250) NOT NULL ,
Code int(20) NOT NULL UNIQUE,
Category varchar(50) NOT NULL,
Price int(10) NOT NULL,
LINK varchar(200)
);
''')
fname='productdetails.csv'
with open(fname, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        id=row[0]
        name=row[1]
        code=row[2]
        cat=row[3]
        price=row[4]
        link=row[5]
        cur.execute('''
        INSERT INTO PRODUCT VALUES(?,?,?,?,?,?)
        ''',(id,name,code,cat,price,link))
        conn.commit()
