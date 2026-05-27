import tkinter as tk
from tkinter import messagebox
import sqlite3
janela = tk.Tk()
janela.title("Controle de Produtos")
conexao = sqlite3.connect("lojas.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT,

    preco REAL

)
""")
conexao.commit()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
entrada_preco = tk.Entry(janela)
entrada_preco.pack()
entrada_id = tk.Entry(janela)
entrada_id.pack()
lista = tk.Listbox(janela, width=50)
lista.pack()
def cadastrar():
    try:

        nome = entrada_nome.get()

        preco = entrada_preco.get()

        if nome == "" or preco == "":

            raise ValueError

        preco = float(preco)

        cursor.execute("""
        INSERT INTO produtos(nome, preco)
        VALUES (?, ?)
        """, (nome, preco))
        conexao.commit()
        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado!"
        )
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preencha os dados corretamente."
        )
def listar():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        texto = (
            f"{produto[0]} - "
            f"{produto[1]} - "
            f"R$ {produto[2]:.2f}"
        )
        texto = texto.replace(".", ",")
        lista.insert(tk.END, texto)
def deletar():
    id_produto = entrada_id.get()
    cursor.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
    conexao.commit()
    messagebox.showinfo("Sucesso","Produto deletado!")
tk.Button(janela,text="Cadastrar",command=cadastrar).pack()
tk.Button(janela,text="Listar",command=listar).pack()
tk.Button(janela,text="Deletar",command=deletar).pack()
janela.mainloop()
