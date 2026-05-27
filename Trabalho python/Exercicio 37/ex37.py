import sqlite3
conexao = sqlite3.connect("Pesquisa.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")
cursor.execute("INSERT INTO produtos(nome) VALUES(?)",("Mouse Gamer",))
cursor.execute("INSERT INTO produtos(nome) VALUES(?)",("Teclado Mecânico",))
cursor.execute("INSERT INTO produtos(nome) VALUES(?)",("Monitor AOC",))
cursor.execute("INSERT INTO produtos(nome) VALUES(?)",("Headset Red Dragon",))
conexao.commit()
termo_pesquisa = input("Digite o nome do produto para pesquisar: ")
cursor.execute("""
SELECT * FROM produtos
WHERE nome LIKE ?
""", (f"%{termo_pesquisa}%",))
produtos = cursor.fetchall()
print(produtos)
conexao.close()