import re
import sqlite3
conexao = sqlite3.connect("dados_web.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS imagens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS links(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT
)
""")
conexao.commit()
with open("Exercicio 46/pagina.html", "r", encoding="utf-8") as file:
    html = file.read()
padrao_img = r'<img[^>]+src="([^"]+)"'
padrao_link = r'<a[^>]+href="([^"]+)"'
imagens = re.findall(padrao_img,html)
links = re.findall(padrao_link,html)
for imagem in imagens:
    url_imagem = imagem.strip()
    cursor.execute("""INSERT INTO imagens(url)VALUES (?) """, (url_imagem,))
for link in links:
    url_link = link.strip()
    cursor.execute("""INSERT INTO links(url)VALUES (?)""", (url_link,))
conexao.commit()
print("Dados salvos no SQLite!")
conexao.close()