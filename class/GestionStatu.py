import psycopg2
from BdConnect import BdConnect
class GestionStatu:
    # def __init__(self):
    #     self.connexion = Connection()

    def insertStatu(self,anaranaStatu):
        bd_connect = BdConnect()
        connection = bd_connect.get_connexion()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO Statut(nomStatut) VALUES (%s)"
            record_to_insert = (anaranaStatu)

            # Exécution de la requête
            cursor.execute(query, record_to_insert)
            connection.commit()
            print("insertion statu reussie")
            self.connexion.disconnect()
        except psycopg2.Error as e:
            print("Erreur lors de l'insertion dans la table statu:", e)

    def makaStatu(self):
        bdconnect = BdConnect()
        try:
            query="SELECT*FROM statut"
            rows = bdconnect.get_result(query)
            statuts = []
            for row in rows:
                statut = {"idStatu": row[0], "typeStatu": row[1]}
                statuts.append(statut)
                print(f"Identifiant: {statut['idStatu']}, Type: {statut['typeStatu']}")
            return statuts
        except psycopg2.Error as e:
            print("Erreur lors de la récupération des statuts:", e)
            return None


if __name__ == "__main__":
    gsStatu = GestionStatu()
    statuts = gsStatu.makaStatu()
    if statuts:
        for statut in statuts:
            print(f"Identifiant: {statut['idStatu']}, Type: {statut['typeStatu']}")
    else:
        print("Aucun statut trouvé.")
    # gsStatu.insertStatu('mpandray')

    # Récupérer et afficher les statuts
    # statuts = gsStatu.makaStatu()
    # if statuts:
    #     for statut in statuts:
    #         print(f"Identifiant: {statut.getId()}, Type: {statut.getType()}")
