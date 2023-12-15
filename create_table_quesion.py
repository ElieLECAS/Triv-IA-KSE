# Python implementation to create a Database in MySQL
import mysql.connector
 
# connecting to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rick3822+",
    database="trivIA_db"
)
 
# cursor object c
c = db.cursor()

questionTable_create = """CREATE TABLE `trivIA_db`.`questions` (
    `id_question` INT NOT NULL AUTO_INCREMENT,
    `categorie` VARCHAR(255) NOT NULL,
    `intitule` TEXT NOT NULL,
    `choix1` VARCHAR(255) NOT NULL,
    `choix2` VARCHAR(255) NOT NULL,
    `choix3` VARCHAR(255) NOT NULL,
    `choix4` VARCHAR(255) NOT NULL,
    `difficulte` ENUM('facile', 'intermediaire', 'difficile') NOT NULL,
    PRIMARY KEY (`id_question`));"""
 
# executing the create database statement
c.execute(questionTable_create)

c = db.cursor()
 
# fetching details
c.execute("desc questions")
 
# printing all details
for i in c:
    print(i)
 
# finally closing the database connection
db.close()