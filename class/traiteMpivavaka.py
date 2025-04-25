from flask import Flask, render_template, request
from GestionStatu import GestionStatu  # Importer la classe GestionStatu
from GestionMpivavaka import GestionMpivavaka
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mpivavaka():
    if request.method == 'POST':
        nom = request.form['Anarana']
        taona = request.form['dtn']
        statu = int(request.form['Statu'])
        gsMpivavaka = GestionMpivavaka()
        gsMpivavaka.insertMpivavaka(nom, taona, statu)
    gsStatu = GestionStatu()
    statuts = gsStatu.makaStatu()  # Récupérer la liste des statuts
    print("bien enregistre")
    return render_template('Mpivavaka.html', statuts=statuts)  # Passer les statuts au template

if __name__ == '__main__':
    app.run(debug=True)