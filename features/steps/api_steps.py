import requests
from behave import given, when, then

# URL base da API
BASE_URL = 'http://localhost:5000/api/pedido'

# Dados do pedido para os testes
PEDIDO_DATA = {
    'id': 1,
    'pedido': 'Produto de Teste',
    'valor': 10.99
}

# Variável para armazenar o URL do QR code de pagamento
qr_code_url = None

@given('um novo pedido com ID, nome e valor')
def step_impl(context):
    # Não é necessário fazer nada aqui, os dados do pedido já estão definidos acima
    pass

@when('faço uma solicitação POST para a API')
def step_impl(context):
    global qr_code_url
    response = requests.post(BASE_URL, json=PEDIDO_DATA)
    assert response.status_code == 200
    qr_code_url = response.json()['qr_code_url']

@then('recebo um código de resposta 200')
def step_impl(context):
    # Não é necessário fazer nada aqui, a verificação já foi feita no passo anterior
    pass

@then('recebo um URL do QR code de pagamento')
def step_impl(context):
    assert qr_code_url is not None

@when('faço uma solicitação GET para a API')
def step_impl(context):
    response = requests.get(BASE_URL)
    context.status_code = response.status_code

@then('recebo um código de resposta 405')
def step_impl(context):
    assert context.status_code == 405

@then('recebo uma mensagem de erro indicando que devo usar o método POST')
def step_impl(context):
    expected_message = 'Use POST method to create a new order.'
    response_message = requests.post(BASE_URL).json()['message']
    assert response_message == expected_message