import tkinter as tk
from tkinter import messagebox
import mysql.connector
import csv
janela = tk.Tk()
janela.title("Executar Query SQL")
tk.Label(janela, text="Host").pack()
entrada_host = tk.Entry(janela)
entrada_host.pack()
tk.Label(janela, text="Usuário").pack()
entrada_user = tk.Entry(janela)
entrada_user.pack()
tk.Label(janela, text="Senha").pack()
entrada_password = tk.Entry(janela,show="*")
entrada_password.pack()
tk.Label(janela, text="Database").pack()
entrada_database = tk.Entry(janela)
entrada_database.pack()
tk.Label(janela, text="Query SQL").pack()
texto_query = tk.Text(
    janela,
    height=10,
    width=50
)
texto_query.pack()
label_resultado = tk.Label(
    janela,
    text=""
)
label_resultado.pack()
def executar_query():
    try:
        host = entrada_host.get()
        user = entrada_user.get()
        password = entrada_password.get()
        database = entrada_database.get()
        query = texto_query.get( "1.0", tk.END)

        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        with open( "resultado_query.csv","w", newline="" ) as arquivo:
            writer = csv.writer(arquivo)
            for linha in resultados:
                writer.writerow(linha)
        label_resultado.config( text="Query executada com sucesso!")
        conexao.close()
    except mysql.connector.Error as erro:
        label_resultado.config(text=f"Erro SQL: {erro}")
botao = tk.Button(janela,text="Executar Query",command=executar_query)
botao.pack()
janela.mainloop()