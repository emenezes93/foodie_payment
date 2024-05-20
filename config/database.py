import psycopg2 , os
from psycopg2 import Error
from datetime import datetime
# Conexão com o banco de dados
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")  
)

def busca_cliente(conn, codigo_cliente):
    try:
        print(codigo_cliente)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM clientes WHERE cpf = %s", (codigo_cliente,))
        cliente = cursor.fetchone()
        if cliente:
            return cliente[0]
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar cliente: {e}")
        return None

# Função para inserir um novo cliente se ele não existir
def verifica_cliente(conn, cpf, nome, email):
    try:
        cursor = conn.cursor()
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO clientes (cpf, nome, email, dtcriacao) VALUES (%s, %s, %s, %s)", (cpf, nome, email, data_formatada))
        conn.commit()
        print("Cliente inserido com sucesso!")

    except Error as e:
        # Em caso de erro, faça rollback da transação
        conn.rollback()
        print(f"Erro ao inserir cliente: {e}")


def insere_pedido(conn, idcliente, token, status):
    try:
        # Verifique se o Pedido já existe
        if not pedido_existe(conn, token):
            # Crie um cursor para executar consultas
            cursor = conn.cursor()
            data_atual = datetime.now()
            data_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")
            # Execute a consulta SQL para inserir o novo pedido
            print ('aqui')
            cursor.execute("INSERT INTO pedidos (idcliente, token, status, dtcriacao) VALUES (%s, %s, %s, %s)", (idcliente, token, status, data_formatada))

            # Confirme a transação
            conn.commit()

            print("Pedido inserido com sucesso!")
        else:
            print("Pedido já existe, não foi necessário inserir.")

    except Error as e:
        # Em caso de erro, faça rollback da transação
        conn.rollback()
        print(f"Erro ao inserir pedido: {e}")

# Função para verificar se o pedido já existe
def pedido_existe(conn, codigo_pedido):
    try:

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE token = %s", (codigo_pedido,))
        Pedido = cursor.fetchone()

        if Pedido:
            return True
        else:
            return False

    except Error as e:
        print(f"Erro ao verificar se o pedido existe: {e}")
        return False
    
# Função para verificar se o pedido já existe e atualizar
def atualiza_status_pedido(conn, codigo_pedido, token_pedido, status_atualizado):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE token = %s", (token_pedido,))
        pedido = cursor.fetchone()

        if pedido:
            # Pedido existe, então execute o UPDATE
            cursor.execute("UPDATE pedidos SET status = %s WHERE token = %s", (status_atualizado, token_pedido))
            conn.commit()
            return True
        else:
            # Pedido não existe
            return False

    except Error as e:
        print(f"Erro ao verificar/atualizar o pedido: {e}")
        conn.rollback()
        return False