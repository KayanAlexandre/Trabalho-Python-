import mysql.connector
mysql = mysql.connector.connect(
host = "localhost",
user = "root",
password = "1234"
)
cursor = mysql.cursor()
cursor.execute("SELECT VERSION()")
versao = cursor.fetchone()
print ("Versao",versao)
mysql.close() 