import sqlite3
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE
)
""")
try:

    cursor.execute("""
    INSERT INTO usuarios(nome, email)
    VALUES(?, ?)
    """, ("Naytan", "naytan@gmail.com"))
    conexao.commit()
    print("Usuário adicionado com sucesso.")
except sqlite3.IntegrityError:
    print("Erro: este email já existe.")
finally:
    conexao.close()