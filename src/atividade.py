import csv

class Atividade:
    def __init__(self,nome,data_fim,peso_aparente,peso_total=0,materia_referente):
        self.materia_referente = materia_referente
        self.peso_total = peso_total
        self.peso_aparente = peso_aparente
        self.data_fim = data_fim
        self.nome = nome

path = "banco.csv"
header = [
    "nome",
    "peso",
    "data",
    "materia"
]
def load_atividades():
    with open("banco.csv") as f:
        pass

def delete_atividades():
    with open("banco.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

def insere_atividade_csv(atividade):
    with open("banco.csv",'a') as f:
        pass
    pass
