import os
import shutil
import sqlite3
from datetime import datetime
import time
conexao = sqlite3.connect("arquivos.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS arquivos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_arquivo TEXT,
    titulo TEXT,
    data_processamento TEXT
)
""")
conexao.commit()
entrada = "entrada"
processados = "processados"
os.makedirs(entrada, exist_ok=True)
os.makedirs(processados, exist_ok=True)
while True:
    for arquivo in os.listdir(entrada):
        if arquivo.endswith(".txt"):
            try:
                caminho = os.path.join(
                    entrada,
                    arquivo
                )
                with open(caminho, "r") as file:
                    titulo = file.readline().strip()
                    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    cursor.execute("""
                    INSERT INTO arquivos(
                        nome_arquivo,
                        titulo,
                        data_processamento
                    )
                    VALUES (?, ?, ?)
                    """, (arquivo, titulo, data))
                    conexao.commit()

                    novo_caminho = os.path.join(processados,arquivo)
                    shutil.move(caminho,novo_caminho)
                    print(f"{arquivo} processado.")
            except Exception as erro:
                print(f"Erro: {erro}")
    time.sleep(5)
