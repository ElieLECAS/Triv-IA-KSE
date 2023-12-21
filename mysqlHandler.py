# # import mysql.connector
# # from mysql.connector import Error
# # import pandas as pd

# class MySQLHandler:
#     def __init__(self, host, user, password, database):
#         try:
#             self.connection = mysql.connector.connect(
#                 host = host,
#                 user = user,
#                 password = password,
#                 database = database
#             )
#             self.cursor = self.connection.cursor()
#         except Error as e:
#             print (f"Erreur MySQL : {e}")


# # Methode de création de la table questions, avec énumérations pour les champs de catégorie et de difficulte
#     def create_table_questions(self):
#         try:
#             questionTbl = """
#                 CREATE TABLE IF NOT EXISTS questions (
#                     id_question INT AUTO_INCREMENT PRIMARY KEY,
#                     intitule varchar(255),
#                     choix1 varchar(255),
#                     choix2 varchar(255),
#                     choix3 varchar(255),
#                     choix4 varchar(255),
#                     categorie ENUM('SQL','Python','Ligne de commandes','Actualités IA', 'Git/GitHub','Thème mystère') NOT NULL,
#                     difficulte ENUM('Facile','Intermediaire','Difficile') NOT NULL
#                 );
#             """
#             self.cursor.execute(questionTbl)
#             self.connection.commit()
#         except mysql.connector.IntegrityError as e:
#             print(f"Erreur d'intégrité MySQL : {e}")


# # Méthode de création de la table reponses, avec idQuestion qui pointe sur l'idQuestion de la table questions
#     def create_table_reponses(self):
#         try:
#             reponseTbl = """
#                 CREATE TABLE IF NOT EXISTS reponses (
#                     id_reponse INT AUTO_INCREMENT PRIMARY KEY,
#                     id_question INT,
#                     reponse_correcte VARCHAR(255),
#                     FOREIGN KEY (id_question) REFERENCES questions(id_question)
#                 );
#             """
#             self.cursor.execute(reponseTbl)
#             self.connection.commit()
#         except mysql.connector.IntegrityError as e:
#             print(f"Erreur d'intégrité MySQL : {e}")



#     # Methode qui permet de fermer la connexion au serveur mysql
#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()



#     # En suivant le modèle CRUD, on créé les méthodes de création, de lecture, de mise à jour et de suppression des différentes itérations de chaque table
#     def create_questions(self, intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte):
#         try:
#             new = """
#                 INSERT INTO questions (intitule, choix1, choix2, choix3, choix4, categorie, difficulte)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#             """
#             values = (intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte)
#             self.cursor.execute(new, values)
#             self.connection.commit()
#         except mysql.connector.ProgrammingError as e:
#             print(f"Erreur de programmation SQL : {e}")


#     def read_questions(self,params):
#         query = """SELECT intitule, choix1, choix2, choix3, choix4 FROM questions WHERE categorie = %s AND difficulte = %s order by rand() limit 1"""
#         self.cursor.execute(query, params)
#         return self.cursor.fetchall()
    

#     def update_questions(self, id_question, new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_categorie, new_difficulte):
#         try:
#             updating = """
#                 UPDATE questions SET
#                 intitule = %s,
#                 choix1 = %s,
#                 choix2 = %s,
#                 choix3 = %s,
#                 choix4 = %s,
#                 categorie = %s,
#                 difficulte = %s WHERE id_question = %d
#             """
#             new_values = (new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_categorie, new_difficulte, id_question)
#             self.cursor.execute(updating, new_values)
#             self.connection.commit()
#         except mysql.connector.ProgrammingError as e:
#             print(f"Erreur de programmation SQL : {e}")

#     def afficher_table(self):
#         self.cursor.execute("DESCRIBE questions;")
#         fields=self.cursor.fetchall()

#         for field in fields:
#             print(field[0])


#     def delete_questions(self, id_question):
#         query = "DELETE FROM questions WHERE id_question = %s"
#         self.cursor.execute(query, id_question)
#         self.connection.commit()

#     def delete_data(self):
#         query = "DROP TABle questions"
#         self.cursor.execute(query)
#         self.connection.commit()

#     def importer_questions_csv(self, file_path):
#         try:
#             # Lire le fichier CSV avec pandas
#             datafile = pd.read_csv(file_path,sep= ';')

#             # Parcourir les lignes du DataFrame et insérer dans la table
#             for index, row in datafile.iterrows():
#                 query = """
#                     INSERT INTO questions (intitule, choix1, choix2, choix3, choix4, categorie, difficulte)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s)
#                 """
#                 values = tuple(row)
#                 self.cursor.execute(query, values)

#             # Commit et fermer la connexion
#             self.connection.commit()
#             print("Importation réussie.")
#         except Exception as e:
#             print(f"Erreur : {e}")


#     def importer_reponses_csv(self, file_path):
#             try:
#                 # Lire le fichier CSV avec pandas
#                 datafile = pd.read_csv(file_path, sep=';')

#                 # Parcourir les lignes du DataFrame et insérer dans la table
#                 for index, row in datafile.iterrows():
#                     query = """
#                         INSERT INTO reponses (id_question, reponse_correcte)
#                         VALUES (%s, %s)
#                     """
#                     values = tuple(row)
#                     self.cursor.execute(query, values)

#                 # Commit
#                 self.connection.commit()
#                 print("Importation réussie.")
#             except Exception as e:
#                 print(f"Erreur : {e}")


# access = MySQLHandler(host='localhost' , user='kevin' , password='Plasma2020@' , database='trivia_db')
# # access.create_table_questions()
# # # access.delete_data()
# # access.create_table_reponses()
# # access.importer_questions_csv('questions.csv')
# # access.importer_reponses_csv('reponses.csv')
# # params=('SQL','Difficile')
# # print(access.read_questions(params))
# # access.afficher_table()
# # access.close_connection()



    

        