import psycopg2

# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="minicurso_db",
                               host="localhost",
                               user="postgres",
                               password="123",
                               port="5432")

    print("Conexão Realizada com sucesso")
    return conexao


# Chame a função para testar a conexão
conexao = conectardb()
