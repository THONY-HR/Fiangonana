from flask import Flask, render_template, request,redirect,url_for
from GestionRakitra import GestionRakitra
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def mpivavaka():
    if request.method=='POST':
        daty=request.form['Daty']
        vola=request.form['montant']
        gsRakitra=GestionRakitra()
        gsRakitra.insertRakitra(vola,daty)
    return render_template('Rakitra.html')
if __name__=='__main__':
    app.run(debug=True)