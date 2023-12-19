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


    def create_table_questions(self):
        questionTbl = """
            CREATE TABLE IF NOT EXISTS questions (
                id_question INT NOT NULL AUTO_INCREMENT,
                id_categorie INT NOT NULL,
                intitule TEXT NOT NULL,
                choix1 VARCHAR(255) NOT NULL,
                choix2 VARCHAR(255) NOT NULL,
                choix3 VARCHAR(255) NOT NULL,
                choix4 VARCHAR(255) NOT NULL,
                id_difficulte INT NOT NULL,
                PRIMARY KEY (id_question),
                FOREIGN KEY (id_categorie) REFERENCES categories(id_categorie),
                FOREIGN KEY (id_difficulte) REFERENCES difficultes(id_difficulte)
            );
        """
        self.cursor.execute(questionTbl)
        self.connection.commit()

    
    def create_table_reponses(self):
        reponseTbl = """
            CREATE TABLE IF NOT EXISTS reponses (
                id_reponse INT NOT NULL AUTO_INCREMENT,
                id_question INT NOT NULL,
                reponse_correcte VARCHAR(255) NOT NULL,
                PRIMARY KEY (id_reponse),
                FOREIGN KEY (id_question) REFERENCES questions(id_question)
            );
        """
        self.cursor.execute(reponseTbl)
        self.connection.commit()

    
    def create_table_categories(self):
        categorieTbl = """
            CREATE TABLE IF NOT EXISTS categories (
                id_categorie INT NOT NULL AUTO_INCREMENT,
                nom VARCHAR(255) NOT NULL,
                PRIMARY KEY (id_categorie)
            );
        """
        self.cursor.execute(categorieTbl)
        self.connection.commit()


    # Methode de création de la table Difficultés, qui prend en compte un ID, et un niveau de difficulté qui sera compris entre 3 différents niveaux
    def create_table_difficultes(self):
        difficulteTbl = """
            CREATE TABLE IF NOT EXISTS difficultes (
                id_difficulte INT NOT NULL AUTO_INCREMENT,
                niveau VARCHAR(255) NOT NULL,
                PRIMARY KEY (id_difficulte)
            );
        """
        self.cursor.execute(difficulteTbl)
        self.connection.commit()


    # Methode qui permet de fermer la connexion au serveur mysql
    def close_connection(self):
        self.cursor.close()
        self.connection.close()




    # En suivant le modèle CRUD, on créé les méthodes de création, de lecture, de mise à jour et de suppression des différentes itérations de chaque table
    def create_questions(self, intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte):
        new = """
            INSERT INTO questions (intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (intitule, choix1, choix2, choix3, choix4, id_categorie, id_difficulte)
        self.cursor.execute(new, values)
        self.connection.commit()


    def read_questions(self):
        query = """SELECT * FROM questions"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    

    def update_questions(self, id_question, new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_id_categorie, new_id_difficulte):
        updating = """
            UPDATE questions SET
            intitule = %s,
            choix1 = %s,
            choix2 = %s,
            choix3 = %s,
            choix4 = %s,
            id_categorie = %d,
            id_difficulte = %d WHERE id_question = %d
        """
        new_values = (new_intitule, new_choix1, new_choix2, new_choix3, new_choix4, new_id_categorie, new_id_difficulte, id_question)
        self.cursor.execute(updating, new_values)
        self.connection.commit()


    def delete_questions(self, id_question):
        query = "DELETE FROM questions WHERE id_question = %s"
        self.cursor.execute(query)
        self.connection.commit()


    def create_categorie(self, nom):
        new = """
            INSERT INTO categories (nom)
            VALUES (%s)
        """
        values = (nom,)
        self.cursor.execute(new, values)
        self.connection.commit()


    def create_difficulte(self, niveau):
        new = """
            INSERT INTO difficultes (niveau)
            VALUES (%s)
        """
        values = (niveau,)
        self.cursor.execute(new, values)
        self.connection.commit()


access = MySQLHandler(host='localhost' , user='root' , password='psswd' , database='trivia_db')
# table = "questions"
access.create_table_categories()
access.create_table_difficultes()
access.create_table_questions()
access.create_table_reponses()
access.create_categorie("Python")
access.create_difficulte("facile")
access.create_questions("quel est le nom du python master ?" , "Kevin" , "Elie" , "Simon" , "Tony" , 0 , 0)
print(access.read_questions())



    

        