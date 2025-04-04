import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select sqlite_version();"

query = "drop table if exists customers"
cursor.execute(query)

<<<<<<< HEAD
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


=======
query = "drop table if exists pets"
cursor.execute(query)

query = "drop table if exists visits"
cursor.execute(query)

###################### customers ###########################
query = """create table customers 
( 
id integer primary key autoincrement, 
fname tinytext, 
lname tinytext,
phone int, 
email tinytext,
address tinytext,
city tinytext,
postalcode tinytext
); 
"""
cursor.execute(query)

data = [
('Jen', 'Mezei', '6042231134', 'jen@shaw.ca',  '891 Cullen Cresc', 'Delta', 'V4L1Q2'),
('John', 'Shu', '6042232255', 'js@shaw.ca',  '123 Dan Rd', 'Surrey', 'V4N1C8')
]

for i in data:
    query = f"insert into customers (fname, lname, phone, email,  address, city, postalcode) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}');"
    cursor.execute(query)

connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()


print ("----------------Initial Customers:------------------");

for i in result:
    print(i)

###################### pets ###########################
query = """create table pets 
( 
    id integer primary key autoincrement, 
    name tinytext,
    type tinytext,
    breed tinytext,
    birthdate tinytext,
    ownerID int
); 
"""
cursor.execute(query)

data = [
('Casey', 'Cat', 'Persion', '2024-10-02', 1),
('Holly', 'Cat', 'Tabby', '2023-01-12', 2)
]

for i in data:
    query = f"insert into pets (name, type, breed, birthdate, ownerID) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}');"
    cursor.execute(query)

connection.commit()
query = "select * from pets"
cursor.execute(query)
result = cursor.fetchall()

print ("----------------Initial Pets:------------------");

for i in result:
    print(i)

###################### visits ###########################
query = """create table visits 
( 
    id integer primary key autoincrement,
    ownerID int,
    petid int,
    details tinytext,
    cost int,
    paid int
); 
"""
cursor.execute(query)

data = [
(1, 1, 'grooming', 23, 20),
(2, 2, 'washing', 50, 50)
]

for i in data:
    query = f"insert into visits (ownerID, petid, details, cost, paid) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}');"
    cursor.execute(query)

connection.commit()
query = "select * from visits"
cursor.execute(query)
result = cursor.fetchall()

print ("----------------Initial Visits:------------------");
for i in result:
    print(i)
    
    
#################  Add a new customer ###################
print ("\n----------------Add a customer :------------------");    

inpt_fname = input("Enter first name: ")
inpt_lname = input("Enter last name: ")
inpt_ph = input("Enter phone: ")
inpt_email = input("Enter email: ")
inpt_addr = input("Enter address: ")
inpt_city = input("Enter city: ")
inpt_pcode = input("Enter postal code: ")

def insert_customer (fname, lname, ph, email, addr, city, pcode):
    cur = connection.cursor()
    cur.execute("insert into customers (fname, lname, phone, email,  address, city, postalcode) values (?,?,?,?,?,?,?);", (fname, lname, ph, email, addr, city, pcode))
    connection.commit()

    
insert_customer(inpt_fname,inpt_lname, inpt_ph ,inpt_email, inpt_addr,inpt_city,inpt_pcode)

query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()

print ("\n----------------After Adding New Customer:------------------");

for i in result:
    print(i)
    
    
#################  Search by email ###################   

def search_customer_by_email (email): 
    cursor = connection.cursor()
    query = """select * from customers where email = ?"""
    cursor.execute(query, (email,))
    records = cursor.fetchall()
    print("Search by email:  ", email)
    for row in records:
        print("First Name = ", row[1])
        print("Last Name  = ", row[2])
    cursor.close()
 
inpt_email = input("Enter email: ")  
search_customer_by_email (inpt_email)  
>>>>>>> 6349b0e6dc7b7542eebdd9e0dbe0b55cc81638c0
