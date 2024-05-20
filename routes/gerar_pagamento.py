import psycopg2
import mercadopago
from config.database import conn, verifica_cliente, insere_pedido, busca_cliente
from flask_restful import Resource, reqparse
# Configurações do Mercado Pago
MERCADO_PAGO_ACCESS_TOKEN = 'TEST-7579327657340780-121907-f489e3c6b1fe98d0cf7207fab993cf6a-259096454'

class Pagamento(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cpf', type=str, required=True, help='CPF do Cliente')
        parser.add_argument('nome', type=str, required=True, help='Nome do Cliente')
        parser.add_argument('email', type=str, required=True, help='E-mail do Cliente')
        parser.add_argument('token', type=str, required=True, help='Id do Pedido Original')
        parser.add_argument('status', type=str, required=True, help='status do Pedido')
        parser.add_argument('codigo', type=str, required=True, help='codigo do Pedido')
        parser.add_argument('valor', type=str, required=True, help='Valor do Pedido')
        args = parser.parse_args()
        qr_code_url = inserir_pedido_e_gerar_qrcode(args['cpf'],args['nome'],args['email'],args['token'],args['status'],args['codigo'],args['valor'])
        if qr_code_url:
            return {'qr_code_url': qr_code_url}, 200
        else:
            return {'message': 'Erro ao inserir o pedido ou gerar o QR code.'}, 400
    #400
    def get(self):
        return {'message': 'Use POST method to create a new order.'}, 405

def inserir_pedido_e_gerar_qrcode(cpf, nome, email, token, status, pedido, valor):
    try:
        cliente = busca_cliente(conn, cpf)
        if cliente is None:
            verifica_cliente(conn, cpf, nome, email)
            cliente = busca_cliente(conn, cpf)
        insere_pedido(conn, cliente, token, status)
        print('chegou4')   
        # Gerar QR code de pagamento do Mercado Pago
        sdk = mercadopago.SDK(MERCADO_PAGO_ACCESS_TOKEN)
        preference_data = {
            "items": [{"title": pedido, "quantity": 1, "currency_id": "BRL", "unit_price": float(valor)}]
        }
        result = sdk.preference().create(preference_data)
        qr_code_url = result['response']['init_point']

        conn.close()

        return qr_code_url
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None