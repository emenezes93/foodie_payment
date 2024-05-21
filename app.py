from flask import Flask
from flask_restful import Api
from routes.gerar_pagamento import Pagamento
from routes.atualizar_pagamento import Atualiza

app = Flask(__name__)
api = Api(app)

api.add_resource(Pagamento, '/api/gerarPagamento')
api.add_resource(Atualiza, '/api/atualizarPagamento')
if __name__ == "__main__":
    app.run(debug=True)