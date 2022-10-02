import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Tkinter2'
    )
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE Registration(firstname VARCHAR(255),lastname VARCHAR(255),address VARCHAR(255),email VARCHAR(255),mobileno BIGINT(255),gender text,country VARCHAR(255),state VARCHAR(255),district VARCHAR(255),pincode int(255),qualification VARCHAR(255))')