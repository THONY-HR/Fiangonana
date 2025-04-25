import psycopg2
from GetDonne import GetDonne
import datetime
getDonne = GetDonne()
# print("vola fiangonana" , getDonne.get_vola_fiangonana())
valeur_initiale = 1485
valeur_finale = 1500
pourcentage = getDonne.calcul_pourcentage(valeur_initiale, valeur_finale)
print(getDonne.manomeDate_getVola(11, 1000,'2024-03-15'))
# print("Le pourcentage entre", valeur_initiale, "Ar et", valeur_finale, "Ar est de :", pourcentage, "%")