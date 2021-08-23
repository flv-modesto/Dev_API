from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id':0,
     'nome':'Alex',
     'habilidades':['Python', 'Flask']
    },
    {
     'id':1,   
     'nome':'Teixeira',
     'habilidades':['Python','Django']}
]

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'. format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrados da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return (response)
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
    
    def delete (self,id):
        desenvolvedores.pop(id)
        return ({'status':'sucesss', 'mensagem':'registro excluido '})

class Lista_Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>/')        
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidade, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)