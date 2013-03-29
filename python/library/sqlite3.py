import sqlite3

#create the connection
conn = sqlite3.connect('/home/halesh/sql')
#create the cursor object and call it's execute
cur = conn.cursor()

#create table
cur.execute('''create  table stock
		(data text,trans text,symbl text,qty real,price real)''')

#Insert a row of data
cur.insert('''insert into stock
	      values('2013-03-30','BUY','RHAT',1000,35.14)''')
conn.commit()
c.close()

