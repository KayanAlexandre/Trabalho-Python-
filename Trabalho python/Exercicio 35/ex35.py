import json
import mysql.connector
with open('Exercicio 35/config.json', 'r') as arquivo:
    config = json.load(arquivo)
    mysql = mysql.connector.connect(
        host = config["host"],
        user = config["user"],
        password = config["password"],
        database = config["database"]
    )
    print("Conexão bem-sucedida!")
    mysql.close()