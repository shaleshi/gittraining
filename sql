SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.

sqlite3 was written by Gerhard Häring and provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249

 conn = sqlite3.connect("mydatabase.db")
>>> cursor = conn.cursor()
>>> cursor.execute("""CREATE TABLE albums (title text, artist text, release_date text, publisher text, media_type text) """)
<sqlite3.Cursor object at 0xa2481e0>
>>> cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
<sqlite3.Cursor object at 0xa2481e0>
>>> conn.commit()
>>> cursor.execuute('select * from albums')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'sqlite3.Cursor' object has no attribute 'execuute'
>>> cursor.execute('select * from albums')
<sqlite3.Cursor object at 0xa2481e0>
>>> a = cursor.execute('select * from albums')
>>> a
<sqlite3.Cursor object at 0xa2481e0>
>>> a.fetchall()
[(u'Glow', u'Andy Hunter', u'7/24/2012', u'Xplore Records', u'MP3')]
>>> 
 sqlite3.connect(database[, timeout, isolation_level, detect_types, factory])

    Opens a connection to the SQLite database file database. You can use ":memory:" to open a database connection to a database that resides in RAM instead of on disk.

dir(sqlite3.Connection)
Connection Objects
Cursor objects
dir(sqlite3.Cursor)

The following Python types can thus be sent to SQLite without any problem:
Python type 	SQLite type
None 	NULL
int 	INTEGER
long 	INTEGER
float 	REAL
str (UTF8-encoded) 	TEXT
unicode 	TEXT
buffer 	BLOB
