from flask_restful import Resource

lista_habilidades = ['Python','Flask', 'Java', 'PHP', 'CCS' ]

class Habilidade(Resource,):
    def get(self):
        return lista_habilidades