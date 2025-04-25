import psycopg2
from BdConnect import BdConnect
from datetime import datetime, timedelta
from datetime import date
class GetDonne:

    def get_vola_fiangonana(self):
        bdconnect = BdConnect()
        query = "SELECT resteVolaFiangonana FROM fiangonanaResteVola"
        result = bdconnect.get_result(query)
        if result and result[0][0] is not None:  # Vérifier si result contient des données et si la valeur n'est pas nulle
            vola_fiangonana = result[0][0]  # Supposant que la requête renvoie une seule valeur
            return vola_fiangonana
        else:
            return None

    def insert_data_into_trosa(self, id_olona, vola_trosa):
        try:
            bd_connect = BdConnect()
            connection = bd_connect.get_connexion()
            cursor = connection.cursor()

            # Requête d'insertion
            insert_query = "INSERT INTO Trosa (idOlona, volaTrosa, dateTrosa) VALUES (%s, %s, %s)"

            # Données à insérer
            record_to_insert = (id_olona, vola_trosa, datetime.now().date())

            # Exécution de la requête
            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            print("Données insérées avec succès dans la table Trosa")

        except Exception as error:
            print("Erreur lors de l'insertion des données dans la table Trosa :", error)

        finally:
            # Fermeture du curseur et de la connexion
            if connection:
                cursor.close()
                connection.close()
                print("Connexion à PostgreSQL fermée")

    def insert_data_into_trosaDate(self, id_olona, vola_trosa, daty):
        try:
            bd_connect = BdConnect()
            connection = bd_connect.get_connexion()
            cursor = connection.cursor()

            # Requête d'insertion
            insert_query = "INSERT INTO Trosa (idOlona, volaTrosa, dateTrosa) VALUES (%s, %s, %s)"

            # Données à insérer
            record_to_insert = (id_olona, vola_trosa, daty)

            # Exécution de la requête
            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            print("Données insérées avec succès dans la table Trosa")

        except Exception as error:
            print("Erreur lors de l'insertion des données dans la table Trosa :", error)

        finally:
            # Fermeture du curseur et de la connexion
            if connection:
                cursor.close()
                connection.close()
                print("Connexion à PostgreSQL fermée")


    def nth_sunday_date(self,n):
        # Obtient la date actuelle
        current_date = datetime.now().date()
        
        # Trouve le jour actuel de la semaine (0 pour lundi, 6 pour dimanche)
        current_weekday = current_date.weekday()
        
        # Calcule le nombre de jours à ajouter pour atteindre le prochain dimanche
        days_until_sunday = 7 - current_weekday
        
        # Calcule la date du prochain dimanche
        next_sunday = current_date + timedelta(days=days_until_sunday)
        
        # Calcule la date du n-ième dimanche
        nth_sunday = next_sunday + timedelta(weeks=n-1)
        
        return nth_sunday

    def calcul_pourcentage(self,valeur_initiale, valeur_finale):
        # Calculer la différence entre la valeur finale et la valeur initiale
        difference = valeur_finale + valeur_initiale/2
        # Calculer le pourcentage en utilisant la formule: (différence / valeur_initiale) * 100
        # pourcentage = (difference / valeur_initiale) * 100
        return difference

    def pourcentage_estimer(self, daty):
        bdconnect = BdConnect()
        # Initialisez la liste pour stocker les valeurs moyennes de volaRakitra
        vola_fiangonana = []
        # Construisez la requête SQL avec la condition WHERE
        query = f"SELECT EXTRACT(YEAR FROM dateRakitra) AS Annee, AVG(volaRakitra) AS Moyenne_Vola FROM Rakitra WHERE dateRakitra < '{daty}' GROUP BY EXTRACT(YEAR FROM dateRakitra);"

        # Exécutez la requête SQL
        result = bdconnect.get_result(query)
        
        # Parcourez les résultats et stockez-les dans la liste vola_fiangonana
        for row in result:
            vola_fiangonana.append(row)

        if vola_fiangonana:
            anne_2022 = vola_fiangonana[2][1]
            anne_2023 = vola_fiangonana[1][1]
            anne_2024 = vola_fiangonana[0][1]

            pourcentage_2022_2023 = self.calcul_pourcentage(anne_2022, anne_2023)
            # pourcentage_2023_2024 = self.calcul_pourcentage(anne_2023, anne_2024)

            # pourcentage_suivant = (pourcentage_2022_2023 + pourcentage_2023_2024) / 2

            # Calculer le pourcentage estimé pour 2024-2025
            # reponse = anne_2024 + (anne_2024 * pourcentage_suivant) / 100
            valony1 = anne_2024 / pourcentage_2022_2023
            reponse = anne_2024 + (anne_2024 * valony1)/2
            # Vérifier si le résultat est négatif et prendre sa valeur absolue si c'est le cas
            if reponse < 0:
                reponse = abs(reponse)

            return reponse

        else:
            return None  # Retournez None si aucun résultat n'est trouvé


    def manomeDate_getVola(self, id_olona, trosaina, daty):
        volaFiangonana = self.get_vola_fiangonana()
        nbrLahady = 0
        current_date = datetime.now().date()
        trosaina = float(trosaina)
        # Obtenez la valeur moyenne de vola par lahady
        moyenne_vola_par_lahady = self.pourcentage_estimer(daty)
        if moyenne_vola_par_lahady != 0:
            if trosaina <= volaFiangonana:
                # Insérer les données dans la table Trosa
                self.insert_data_into_trosa(id_olona, trosaina)
                current_date = datetime.now().date()
            else:
                # Calculer le nombre de lahady nécessaires pour atteindre trosaina
                while volaFiangonana < trosaina:
                    volaFiangonana += moyenne_vola_par_lahady
                    nbrLahady += 1
                current_date = self.nth_sunday_date(nbrLahady)
                self.insert_data_into_trosaDate(id_olona,trosaina,current_date)
            return current_date
        return "Tsy afaka mihindrana aloha"