# Python implementation to create a Database in MySQL
import mysql.connector
 
# connecting to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="kevin",
    passwd="Plasma2020@"
)
 
# cursor object c
c = db.cursor()
 
# executing the create database statement
c.execute("CREATE DATABASE IF NOT EXISTS trivia_db")
 
# fetching all the databases
c.execute("SHOW DATABASES")
 
# printing all the databases
for i in c:
    print(i)

c = db.cursor()
 
# finally closing the database connection
db.close()