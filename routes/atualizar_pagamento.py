from flask_restful import Resource, reqparse
from config.database import conn , atualiza_status_pedido

class Atualiza(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('codigo', type=str, required=True, help='Codigo do Pedido')
        parser.add_argument('token', type=str, required=True, help='token do Pedido')
        parser.add_argument('status', type=str, required=True, help='status do Pedido')
        args = parser.parse_args()
        
        qr_code_url = atualiza_status_pedido(conn,args['codigo'], args['token'],args['status'])
        if qr_code_url:
            return {'message': 'Status atualizado com Sucesso.' }, 200
        else:
            return {'message': 'Erro ao atualizar o status do pedido.'}, 400

    def get(self):
        return {'message': 'Use POST method to create a new order.'}, 405