import csv

header = [
    "nome_atividade",
    "data_fim", 
    "peso_atividade",
    "materia"
]
def load_atividades():
    atividades = []
    with open("banco.csv",'r') as f:
        # pula o header do csv
        next(f)
        for l in f.readlines():
            dc = {}
            l = l.split(",")
            dc["nome_atividade"] = l[0]
            dc["data_fim"] = l[1]
            dc["peso_atividade"] = l[2]
            dc["materia"] = l[3][:-1]
            atividades.append(dc)
    return atividades


def delete_atividades():
    with open("banco.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

def insere_atividade_csv(atividade):
    atividade = [atividade]
    with open("banco.csv",'a') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writerows(atividade)
