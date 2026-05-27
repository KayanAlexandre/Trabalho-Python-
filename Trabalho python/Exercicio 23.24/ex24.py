import mysql.connector
mysql = mysql.connector.connect(
host = "localhost",
user = "root",
password = "1234",
database = "escola"
)
cursor = mysql.cursor()
cursor.execute("""
CREATE TABLE if not exists Clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
)
""")
print("Tabela criada")
mysql.close()