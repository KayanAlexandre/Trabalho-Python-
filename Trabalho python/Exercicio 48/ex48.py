import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
import hashlib
from datetime import datetime
import threading
janela = tk.Tk()
janela.title("Login Corporativo")
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="empresa"
)
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255)
)
""")
conexao.commit()
senha_hash = hashlib.sha256("1234".encode()).hexdigest()

try:
    cursor.execute("""
    INSERT INTO usuarios(email, senha)
    VALUES(%s, %s)
    """, (
        "admin@gmail.com",
        senha_hash
    ))
    conexao.commit()
except:
    pass
tk.Label(janela,text="E-mail").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()
tk.Label(janela,text="Senha").pack()
entrada_senha = tk.Entry(janela,show="*")
entrada_senha.pack()
def salvar_log(email, resultado):
    with open("auditoria.log","a",encoding="utf-8") as file:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f"{data} | "f"{email} | "f"{resultado}\n")
def login():
    try:
        email = entrada_email.get()
        senha = entrada_senha.get()
        padrao = r"\S+@\S+\.\S+"
        if not re.match(padrao, email):
            raise ValueError("E-mail inválido")
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        cursor.execute("""
        SELECT * FROM usuarios
        WHERE email=%s AND senha=%s
        """, (email, senha_hash))
        usuario = cursor.fetchone()
        if usuario:
            messagebox.showinfo("Login","Login realizado!")
            threading.Thread( target=salvar_log,args=(email, "SUCESSO")).start()
        else:
            messagebox.showerror("Erro","Credenciais inválidas")
            threading.Thread(target=salvar_log,args=(email, "FALHA")).start()
    except ValueError as erro:
        messagebox.showerror("Erro",str(erro))
botao = tk.Button(janela,text="Entrar",command=login)
botao.pack()
janela.mainloop()
conexao.close()