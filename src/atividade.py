import csv

header = [
    "nome_atividade",
    "data_fim", 
    "peso_atividade",
    "materia"
]
def load_atividades():
    reader = None
    with open("banco.csv",'r') as f:
        reader = csv.DictReader(f)
    print(reader)
    return reader


def delete_atividades():
    with open("banco.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

def insere_atividade_csv(atividade):
    atividade = [atividade]
    with open("banco.csv",'a') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writerows(atividade)
