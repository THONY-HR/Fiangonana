from flask import Flask, render_template

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route
@app.route('/')
def hello_world():
    essayer = test()
    return render_template('index.html')

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
