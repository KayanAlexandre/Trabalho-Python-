import psycopg2
conexao = psycopg2.connect(
    host="localhost",
    database="banco",
    user="postgres",
    password="1234"
)
cursor = conexao.cursor()
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas_bancarias(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100),
        saldo NUMERIC
    )
    """)
    cursor.execute("""
    UPDATE contas_bancarias
    SET saldo = saldo - 200
    WHERE id = 1
    """)
    cursor.execute("""
    UPDATE contas_bancarias
    SET saldo = saldo + 200
    WHERE id = 2
    """)
    conexao.commit()
    print("Transferência realizada com sucesso!")
except Exception:
    conexao.rollback()
    print("Erro ao realizar a transferência.")
conexao.close()