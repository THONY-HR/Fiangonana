import psycopg2
from BdConnect import BdConnect
class GestionMpivavaka:
    # def __init__(self):
    #     self.connexion = BdConnect()
    def insertMpivavaka(self,anarana,age,statu):
        bd_connect = BdConnect()
        connection = bd_connect.get_connexion()
        cursor = connection.cursor()
        try:
            requete="INSERT INTO Olona(idOlona,nomOlona,anneeDeNaissance,idStatut) VALUES(nextval('mpivavakaId'),%s,%s,%s)"
            # self.connexion.cur.execute(requete,(anarana,age,statu))
            # self.connexion.conn.commit()
            # Données à insérer
            record_to_insert = (anarana, age, statu)

            # Exécution de la requête
            cursor.execute(requete, record_to_insert)
            connection.commit()
            print("isertion mpivavaka reussie")
            # self.connexion.disconnect()
        except psycopg2.Error as e:
            print("Erreur lors de l'insertion dans la table mpivavaka:", e)

    def getMpivavaka(self):
        bdconnect = BdConnect()
        try:
            query="SELECT idOlona, nomOlona FROM Olona WHERE idStatut=2"
            rows = bdconnect.get_result(query)
            mpivavakas = []
            for row in rows:
                mpivavaka = {"idOlona": row[0], "anarana": row[1]}
                mpivavakas.append(mpivavaka)
                print(f"ID Olona: {mpivavaka['idOlona']}, Anarana: {mpivavaka['anarana']}")
            return mpivavakas
        except psycopg2.Error as e:
            print("Erreur lors de la récupération des données mpivavaka:", e)
            return None

if __name__ == "__main__":
    gsMpivavaka = GestionMpivavaka()
    mp=gsMpivavaka.getMpivavaka()
    if mp:
        for m in mp:
            print(f"ID Olona: {m['idOlona']}, Anarana: {m['anarana']}")
#     gsMpivavaka.insertMpivavaka("Rakoto","2024-03-05",1)


    # def listeMpivavaka(self):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute('select* from mpivavaka')
    #         rows=self.cur.fetchall()
    #         return rows
    #     except psycopg2.Error as e:
    #         return None
    #     connexion.disconnect()
        
    # def demande(self,olona,daty,valeur):
        # moyenne=moyenneParMois()
        # datyAzahona
        # insertion demande