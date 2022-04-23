import json

class Materia:
    def __init__(self,id_,title,prerequisites,period,credits):
        self.credits = credits
        self.period = period
        self.prerequisites = prerequisites
        self.title = title
        self.id_ = id_

path_curso = "cursos/engenharia_software.json"
def load_materias():
    data = None
    materias = []
    with open(path_curso) as f:
        data = json.loads(f.read())
        for m in data['root']:
            materias.append(
                Materia(id_=m['id'],
                    title = m['title'],
                    prerequisites = m['prerequisites'],
                    period = m['period'],
                    credits = m['credits']
                ))
    return materias
