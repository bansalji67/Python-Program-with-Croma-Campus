import mysql.connector

class DBConnect:
    def getConnection():
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='553655',
            database='amazon'
        )
        return conn