from flask import Flask, render_template, request, redirect, url_for
from GestionMpivavaka import GestionMpivavaka
from GetDonne import GetDonne

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def manaoDemande():
    if request.method == 'POST':
        idOlona = int(request.form['membre'])
        volaIlaina = request.form['vola']
        dateDemande = request.form['dateNow']
        gd = GetDonne()
        datyAzonaVola = gd.manomeDate_getVola(idOlona, volaIlaina, dateDemande)
        gd.insert_data_into_trosa(idOlona, dateDemande)
        return str(datyAzonaVola)  # Convertir la date en chaîne de caractères
        
    # Récupérer la liste des mpivavaka
    gsMpivavaka = GestionMpivavaka()
    mpivavakas = gsMpivavaka.getMpivavaka()
    
    return render_template('demande.html', mpivavakas=mpivavakas)

if __name__ == '__main__':
    app.run(debug=True)

