"""
first install the packages
pip install pyodbc
pip install sqlalchemy
"""

# Building a connection and  cursor with SQLEXPRESS

import pyodbc
print(pyodbc.drivers())
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;',
    autocommit=True
)
cur=connection.cursor()
print(cur)
#========================================================
"""
# How to create a Database

cur.execute("CREATE DATABASE amazon")
print("Database created successfully")

# How to create a table
  cur.execute(""" 

#CREATE TABLE employee(eid int PRIMARY KEY,
#                      ename VARCHAR(100),
#                      eadd VARCHAR(100),
#                      esal DECIMAL(8,2)
#                     )""")
#connection.commit()
#print("Table Create Successfully")
"""
# How to insert the record

import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

cur = connection.cursor()

sql = "INSERT INTO employee(eid,ename,eadd,esal) VALUES (?,?,?,?)"

cur.execute(sql, (102, 'Ajay Kumar', 'GZH', 5677.3))

connection.commit()

print("Record Inserted Successfully")


# Insert Records by User

import pyodbc
print(pyodbc.drivers())
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;',
    autocommit=True
)
cur=connection.cursor()
print(cur)

eid =  input("Enter Employee ID : ")
ename = input("Enter the Employee Name : ")
eadd  = input("Enter the Employee Address : ")
esal  = input("Enter the Employee Salary : ")

sql = "insert into employee values(?,?,?,?)"
data= (eid,ename,eadd,esal)
cur.execute(sql,data)
connection.commit()

# READ DATA FROM DATABASE

import pyodbc
print(pyodbc.drivers())
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;',
    autocommit=True
)
cur=connection.cursor()
print(cur)

sql="Select * from employee"
cur.execute(sql)
data=cur.fetchall()
for emp in data:
    print(emp[0],'\t',emp[1],'\t',emp[2],'\t',emp[3])

# DELETE THE RECORDS FROM THE TABLE

import pyodbc
print(pyodbc.drivers())
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;',
    autocommit=True
)
cur=connection.cursor()
print(cur)

sql='delete from employee where eid=105'
cur.execute(sql)
connection.commit()

# UPDATE RECORD IN A TABLE

import pyodbc
print(pyodbc.drivers())
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;',
    autocommit=True
)
cur=connection.cursor()
print(cur)

sql='update employee set esal=60000 where eid=102'
cur.execute(sql)
connection.commit()
"""








