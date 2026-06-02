import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=amazon;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

cur = connection.cursor()

class DBConnect:
    def getconnection():
        cur = connection.cursor()
        print(cur)
DBConnect.getconnection()