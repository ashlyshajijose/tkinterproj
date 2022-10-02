import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='datab'
    )
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE register(fname VARCHAR(255),lname VARCHAR(255),addr VARCHAR(255),emid VARCHAR(255),mob VARCHAR(255),birth varchar(255),gen varchar(100),educ varchar(255))')

