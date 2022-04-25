from flask import Flask, render_template, request
from materia import load_materias
from atividade import load_atividades,delete_atividades,insere_atividade_csv, weight_dfs

import os

app = Flask(__name__)

@app.route("/")
def index():
    titulo_id_materias = [(m.title,m.id_) for m in load_materias()]
    return render_template('home.html',titulo_id_materias=titulo_id_materias)

@app.route("/agenda")
def agenda():
    atividades = load_atividades()
    return render_template('to_do_list.html',atividades=atividades)
    
@app.route("/insere_atividade", methods=['POST'])
def insere_atividade():
    insere_atividade_csv(request.form)
    return render_template('home.html')

@app.route("/remove_todas_atividades", methods=['POST'])
def remove_todas_atividades():
    delete_atividades()
    titulo_id_materias = [(m.title,m.id_) for m in load_materias()]
    return render_template('home.html',titulo_id_materias=titulo_id_materias)

@app.route("/ordena_atividades", methods=['POST'])
def ordena_atividades():
    atividades = load_atividades()
    weighted_act = []
    for a in atividades:
        output =  weight_dfs(int(a["peso_atividade"]), a["materia"])
        a["peso_final"] = output[0]
        a["trancadas"] = output[1]
        weighted_act.append(a)
    weighted_act = sorted(weighted_act, key=lambda d: d['peso_final'], reverse=True) 
    return render_template('to_do_list.html', atividades=weighted_act)

if __name__ == "__main__":
    app.run(debug=False)
