import mysql.connector

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connection.cursor()

# Methode de création de la table questions, avec énumérations pour les champs de catégorie et de difficulte
    def create_table_questions(self):
        questionTbl = """
            CREATE TABLE IF NOT EXISTS questions (
                id_question INT AUTO_INCREMENT PRIMARY KEY,
                intitule varchar(255),
                choix1 varchar(255),
                choix2 varchar(255),
                choix3 varchar(255),
                choix4 varchar(255),
                categorie ENUM('SQL','Python','Ligne de commandes','Actualités IA', 'Git/GitHub','Thème mystère') NOT NULL,
                difficulte ENUM('Facile','Intermediaire','Difficile') NOT NULL
            );
        """
        self.cursor.execute(questionTbl)
        self.connection.commit()

# Méthode de création de la table reponses, avec idQuestion qui pointe sur l'idQuestion de la table questions
    def create_table_reponses(self):
        reponseTbl = """
            CREATE TABLE IF NOT EXISTS reponses (
                id_reponse INT AUTO_INCREMENT PRIMARY KEY,
                id_question INT,
                reponse_correcte VARCHAR(255),
                FOREIGN KEY (id_question) REFERENCES questions(id_question)
            );
        """
        self.cursor.execute(reponseTbl)
        self.connection.commit()



    # Methode qui permet de fermer la connexion au serveur mysql
    def close_connection(self):
        self.cursor.close()
        self.connection.close()



    # En suivant le modèle CRUD, on créé les méthodes de création, de lecture, de mise à jour et de suppression des différentes itérations de chaque table
    def create_questions(self, intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte):
        new = """
            INSERT INTO questions (intitule, choix1, choix2, choix3, choix4, categorie, difficulte)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte)
        self.cursor.execute(new, values)
        self.connection.commit()


    def read_questions(self,params):
        query = """SELECT intitule, choix1, choix2, choix3, choix4 FROM questions WHERE categorie = %s AND difficulte = %s"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    

    def update_questions(self, id_question, new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_categorie, new_difficulte):
        updating = """
            UPDATE questions SET
            intitule = %s,
            choix1 = %s,
            choix2 = %s,
            choix3 = %s,
            choix4 = %s,
            categorie = %s,
            difficulte = %s WHERE id_question = %d
        """
        new_values = (new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_categorie, new_difficulte, id_question)
        self.cursor.execute(updating, new_values)
        self.connection.commit()


    def delete_questions(self, id_question):
        query = "DELETE FROM questions WHERE id_question = %s"
        self.cursor.execute(query, id_question)
        self.connection.commit()



access = MySQLHandler(host='localhost' , user='root' , password='psswd' , database='trivia_db')
access.create_table_questions()
access.create_table_reponses()
print(access.read_questions())



    

        