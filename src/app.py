from flask import Flask, render_template, request
from materias import load_materias

import os

app = Flask(__name__)

@app.route("/")
def index():
    titulo_id_materias = [(m.title,m.id_) for m in load_materias()]
    return render_template('home.html',titulo_id_materias=titulo_id_materias)

@app.route("/agenda")
def agenda():
    return render_template('to_do_list.html')
@app.route("/insere_atividade", methods=['POST'])
def insere_atividade():
    pass

@app.route("/remove_todas_atividades", methods=['POST'])
def remove_todas_atividades():
    pass

if __name__ == "__main__":
    app.run(debug=False)
