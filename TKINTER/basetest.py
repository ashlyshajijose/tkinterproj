import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Tkinter3'
    )
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE register(fname VARCHAR(255),lname VARCHAR(255),addr VARCHAR(255),emid VARCHAR(255),mob VARCHAR(255),birth VARCHAR(255),gen VARCHAR(100),educ VARCHAR(255))')

