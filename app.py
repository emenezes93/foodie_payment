from flask import Flask
from flask_restful import Api
from routes.pagamento import Pagamento
from routes.atualiza_pedido import Atualiza

app = Flask(__name__)
api = Api(app)

api.add_resource(Pagamento, '/api/pedido')
api.add_resource(Atualiza, '/api/atualizaPedido')
if __name__ == "__main__":
    app.run(debug=True)