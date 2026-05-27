import os
import json
import mysql.connector
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="vendas"
    )
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas(

        id INT AUTO_INCREMENT PRIMARY KEY,

        produto VARCHAR(100),

        valor FLOAT
    )
    """)
    pasta = "json_vendas"
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".json"):
            with open(
                os.path.join(pasta, arquivo),
                "r"
            ) as file:
                dados = json.load(file)
                valores = []
                for venda in dados:
                    valores.append(
                        (
                            venda["produto"],
                            venda["valor"]
                        )
                    )
                cursor.executemany("""
                INSERT INTO vendas(produto, valor)
                VALUES (%s, %s)
                """, valores)
                conexao.commit()
                print("Dados inseridos com sucesso.")

except json.JSONDecodeError:
    print("Erro no JSON")
except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    cursor.close()
    conexao.close()