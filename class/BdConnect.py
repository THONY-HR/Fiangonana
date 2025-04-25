import psycopg2
class BdConnect:
    def __init__(self):
        try:
            # Initialisez votre connexion ici
            self.connexion = psycopg2.connect(
                user="postgres",
                password="031013",
                host="localhost",
                port="5432",
                database="fiangonana"
            )
            self.preparedStatement = None
            self.result = None
        except psycopg2.Error as e:
            print("Erreur lors de la connexion à PostgreSQL :", e)

    def get_prepa_statement(self):
        return self.preparedStatement

    def set_prepa_statement(self, state_query):
        self.preparedStatement = state_query

    def get_connexion(self):
        return self.connexion

    def get_result(self, requete_jsp):
        try:
            # Exécutez la requête directement
            with self.connexion.cursor() as cur:
                cur.execute(requete_jsp)
                self.result = cur.fetchall()
            return self.result
        except psycopg2.Error as e:
            print("Erreur lors de l'exécution de la requête :", e)

    def close_serv(self):
        try:
            if self.connexion is not None:
                self.connexion.close()
        except psycopg2.Error as e:
            print("Erreur lors de la fermeture de la connexion :", e)
