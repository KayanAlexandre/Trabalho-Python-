import psycopg2
conexao = psycopg2.connect(
    host = "localhost",
    database ="postgres",
    user = "postgres",
    password = "1234"
)
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
                   id SERIAL PRIMARY KEY,
                   nome VARCHAR(100),
                   preco NUMERIC
                   )
                   """)
conexao.commit()
print("Tabela criada")
conexao.close()