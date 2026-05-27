import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import re
import os
from datetime import datetime

janela = tk.Tk()
janela.title("Dashboard Desktop")
janela.geometry("900x600")
os.makedirs(
    "logs_erro",
    exist_ok=True
)
conexao = sqlite3.connect(
    "dashboard.db"
)
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT,

    email TEXT
)
""")
conexao.commit()
def salvar_log(erro):
    data = datetime.now().strftime(
        "%d-%m-%Y_%H-%M-%S"
    )
    caminho = (f"logs_erro/log_{data}.txt")
    with open(caminho, "w",encoding="utf-8") as file:
        file.write(str(erro))
frame1 = tk.Frame(janela,bd=2,relief="solid")
frame1.place(x=10,y=10,width=420, height=250)
frame2 = tk.Frame(janela,bd=2,relief="solid")
frame2.place(x=450,y=10,width=420,height=250)
frame3 = tk.Frame(janela,bd=2,relief="solid")
frame3.place(x=10,y=280,width=860,height=250)
lista = tk.Listbox(frame2,width=60)
lista.pack(pady=10)
def listar_dados():
    try:
        lista.delete( 0, tk.END)
        cursor.execute("""
        SELECT * FROM registros
        """)
        dados = cursor.fetchall()
        for dado in dados:
            texto = (f"{dado[0]} | " f"{dado[1]} | " f"{dado[2]}" )
            lista.insert(tk.END,texto)
    except Exception as erro:
        salvar_log(erro)
def carregar_arquivo():
    try:
        arquivo = filedialog.askopenfilename(
            filetypes=[
                ("Arquivo TXT", "*.txt")
            ]
        )
        with open( arquivo, "r",encoding="utf-8") as file:
            for linha in file:
                partes = linha.strip().split(",")
                if len(partes) != 2:
                    raise ValueError("Linha inválida")
                nome = partes[0].strip()
                email = partes[1].strip()
                padrao = r"\S+@\S+\.\S+"
                if not re.match(padrao,email):
                    raise ValueError("E-mail inválido")
                cursor.execute("""
                INSERT INTO registros(
                    nome,
                    email
                )
                VALUES (?, ?)
                """, (
                    nome,
                    email
                ))
        conexao.commit()
        listar_dados()
        messagebox.showinfo("Sucesso","Dados importados!" )
    except Exception as erro:
        salvar_log(erro)
        messagebox.showerror( "Erro",str(erro))
def pesquisar():
    try:
        termo = entrada_pesquisa.get()
        lista.delete( 0,tk.END)
        cursor.execute("""
        SELECT * FROM registros
        """)
        dados = cursor.fetchall()
        for dado in dados:
            texto = ( f"{dado[0]} | " f"{dado[1]} | "f"{dado[2]}")
            if re.search(
                termo,
                texto,
                re.IGNORECASE):
                lista.insert(tk.END,texto )
    except Exception as erro:
        salvar_log(erro)
        messagebox.showerror( "Erro",str(erro))
botao_importar = tk.Button(frame1,text="Importar TXT",command=carregar_arquivo)
botao_importar.pack(pady=20)
tk.Label(frame3,text="Pesquisar").pack()
entrada_pesquisa = tk.Entry(frame3,width=40)
entrada_pesquisa.pack(pady=10)
botao_pesquisa = tk.Button(frame3,text="Buscar",command=pesquisar)
botao_pesquisa.pack()
listar_dados()
janela.mainloop()
conexao.close()