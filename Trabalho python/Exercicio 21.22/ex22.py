import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute("SELECT AVG(nota) FROM ALUNOS")
media = cursor.fetchone()
print("Media: ", media[0])
conexao.close()