import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select sqlite_version();"

query = "drop table if exists customers"
cursor.execute(query)

query = """create table customers
( 
id integer primary key autoincrement, 
fname tinytext,
lname tinytext, 
phone int,
email int, 
address int,
city tinytext,
postalcode int); """
cursor.execute(query)


query = "drop table if exists pets"
cursor.execute(query)

query = """create table pets
( 
id integer primary key autoincrement, 
pname tinytext,
type tinytext, 
breed tinytext,
birthdate int, 
ownerID int); """
cursor.execute(query)

query = "drop table if exists visits"
cursor.execute(query)

query = """create table visits
( 
id integer primary key autoincrement, 
pname tinytext,
type tinytext, 
breed tinytext,
birthdate int, 
ownerID int); """
cursor.execute(query)


