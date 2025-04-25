import psycopg2
from BdConnect import BdConnect
class GestionRakitra:
    # def __init__(self):
    #     self.connexion = Connection()

    def insertRakitra(self, rakitra, date_alahady):
        bd_connect = BdConnect()
        connection = bd_connect.get_connexion()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO rakitra (volaRakitra, dateRakitrab) VALUES (%s, %s)"
            record_to_insert = (rakitra, date_alahady)

            # Exécution de la requête
            cursor.execute(query, record_to_insert)
            connection.commit()
            print("insertion rakitra reussie")
            # self.connexion.disconnect()
        except psycopg2.Error as e:
            print("Erreur lors de l'insertion dans la table rakitra:", e)

    # def moyenneRakitra2022(self):
    #     self.connexion.connect()
    #     try:
    #         query="SELECT AVG(rakitra) AS moyenneRakitra FROM rakitra where"
    #         self.connexion.cur.execute(query)
    #         rakitra=self.connexion.cur.fetchone()
    #         if rakitra:
    #             valiny=rakitra[0]
    #             return valiny
    #     except psycopg2.Error as e:
    #         print("Erreur pour la moyenne de rakitra", e)
    #     finally:
    #         self.connexion.disconnect()

    # def rakitraFarany(self):
    #     self.connexion.connect()
    #     try:
    #         query="SELECT rakitra FROM rakitra order by dateAlahady DESC LIMIT 1"
    #         self.connexion.cur.execute(query)
    #         rakitra=self.connexion.cur.fetchone()
    #         if rakitra:
    #             valiny=rakitra[0]
    #             return valiny
    #     except psycopg2.Error as e:
    #         print("Erreur pour la moyenne de rakitra", e)
    #     finally:
    #         self.connexion.disconnect()

    # def sumRakitra(self):
    #     self.connexion.connect()
    #     try:
    #         query="SELECT SUM(rakitra) AS sommeRakitra FROM rakitra"
    #         self.connexion.cur.execute(query)
    #         rakitra=self.connexion.cur.fetchone()
    #         if rakitra:
    #             valiny=rakitra[0]
    #             return valiny
    #     except psycopg2.Error as e:
    #         print("Erreur pour la somme de rakitra", e)
    #     finally:
    #         self.connexion.disconnect()


    # def nombreDeJourEstimer(self, volaDemande):
    #     somme = self.sumRakitra()
    #     rakitra = self.rakitraFarany()
    #     boucle = 0
    #     while somme < volaDemande:
    #         somme += rakitra
    #         boucle += 1
    #     return boucle

if __name__ == "__main__":
    gestion_rakitra = GestionRakitra()
    gestion_rakitra.insertRakitra(5000, "2024-03-10")
    # print("somme: ",gestion_rakitra.sumRakitra())
    # print("moyenne: ",gestion_rakitra.moyenneRakitraAlahady())
    # print("nb mois",gestion_rakitra.nombreDeJourEstimer(190000))

# import psycopg2
# class GestionRakitra:
#     def __init__(self):
#         self.connexion=Connection()
    # def insertRakitra(self,vola,daty):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute("INSERT INTO rakitra values")
    #     except psycopg2.Error as e:
    # def insertRakitra(self, rakitra, date_alahady):
    #     self.connexion.connect()
    #     try:
    #         query = "INSERT INTO rakitra (rakitra, dateAlahady) VALUES (%s, %s)"
    #         self.connexion.cur.execute(query, (rakitra, date_alahady))
    #         self.conn.commit()
    #         print("Données insérées avec succès dans la table rakitra")
    #     except psycopg2.Error as e:
    #         print("Erreur lors de l'insertion dans la table rakitra:", e)

    # gestion_rakitra=GestionRakitra()
    # gestion_rakitra.insertRakitra(5000,"2024-03-05")

# connexion=gestion_rakitra.connexion
# connexion.connect()
# connexion.cur.execute("select*from rakitra")
# rows=connexion.cur.fetchall()
# for row in rows:
#     print(row)
# connexion.disconnect()
    
    # def resteVolaFiangonana(self):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute('select* from gestionVola ')

    # def pourcentageVola2023(self):

    # def pourcentageVola2024(self):
    
    # def moyenneParMois(self):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute('select AVG(rakitra) from rakitra ')
    # def moyenneFevrier(self):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute('select AVG(rakitra) from rakitra ')
    # def moyenneJanvier(self):
    #     connexion=Connection()
    #     connexion.connect()
    #     try:
    #         self.cur.execute('select AVG(rakitra) from rakitra ')

    # def differenceEntre2mois(self):
        # moyenne=moyenneFevrier()-moyenneJanvier()
        # return moyenne
        # moyenne %fevrier-%janvier

    # def pourcentAvenir(self):
        # vola= resteVolaFiangonana()+differenceEntre2mois()
        # return vola 