from behave import given, when, then
import requests

@given('que eu tenho os dados para gerar um pagamento')
def step_impl(context):
    context.payload = {
        'cpf': '123.456.789-10',
        'nome': 'Fulano',
        'email': 'fulano@example.com',
        'token': 'abc123',
        'status': 'pendente',
        'codigo': '789',
        'valor': '100.00'
    }

@when('eu faço uma solicitação para gerar um pagamento')
def step_impl(context):
    url = 'http://localhost:5000/api/api/gerarPagamento'
    response = requests.post(url, json=context.payload)
    context.response = response

@then('a resposta deve conter um código de status 200')
def step_impl(context):
    assert context.response.status_code == 200

@then('o pagamento deve ser gerado com sucesso')
def step_impl(context):
    assert 'message' in context.response.json()

@given('que eu tenho os dados para atualizar um pagamento')
def step_impl(context):
    context.payload = {
        'codigo': '789',
        'token': 'abc123',
        'status': '1'
    }

@when('eu faço uma solicitação para atualizar um pagamento')
def step_impl(context):
    url = 'http://localhost:5000/api/atualizarPagamento'
    response = requests.post(url, json=context.payload)
    context.response = response

@then('o pagamento deve ser atualizado com sucesso')
def step_impl(context):
    assert context.response.status_code == 200

@then('uma mensagem de erro deve ser retornada')
def step_impl(context):
    assert context.response.status_code == 400
    assert 'message' in context.response.json()

@given('que eu tenho dados inválidos para atualizar um pagamento')
def step_impl(context):
    context.payload = {
        'codigo': '789',
        'status': 'pago'
    }

@given('que eu tenho dados incompletos para gerar um pagamento')
def step_impl(context):
    context.payload = {
        'cpf': '123.456.789-10',
        'nome': 'Fulano',
        'email': 'fulano@example.com',
        'status': 'pendente',
        'codigo': '789',
        'valor': '100.00'
    }