from plateau import Plateau
from mysqlHandler import MySQLHandler


access = MySQLHandler(host='localhost' , user='kevin' , password='Plasma2020@' , database='trivia_db')   
plateau1 = Plateau(access)
plateau1.peupler_le_plateau(int(input("Combien de joueurs : ")))
plateau1.deroulement()