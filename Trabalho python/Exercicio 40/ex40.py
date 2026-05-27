import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
janela = tk.Tk()
janela.title("Cadastro de Usuário")
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cpf TEXT UNIQUE
            )""")
conexao.commit()
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
tk.Label(janela, text="Email").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()
tk.Label(janela, text="CPF:").pack()
entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()
def salvar():
    nome= entrada_nome.get()
    email = entrada_email.get()
    cpf = entrada_cpf.get()
    try:
        padrao_email = r"\S+@\S+\.\S+"
        padrao_cpf = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
        if not re.match(padrao_email, email):
            raise ValueError("Email inválido.")
        if not re.match(padrao_cpf, cpf):
            raise ValueError("CPF inválido.")
        cursor.execute("""INSERT INTO usuarios(nome, email, cpf)values(?, ?, ?)""", (nome, email, cpf))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já cadastrado.")
    except ValueError as erro:
        messagebox.showerror("Erro", str(erro))
botao = tk.Button(janela, text="Salvar", command=salvar)
botao.pack()
janela.mainloop()
conexao.close()