import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Tela login")
def login():
    try:

        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario == "" or senha == "":
            raise ValueError
        messagebox.showinfo(
            "Login",
            "Login realizado com sucesso!"
        )
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos!"
        )
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

entrada_senha = tk.Entry(janela)
entrada_senha.pack()
botao = tk.Button(janela, text="Login", command=login)
botao.pack()
janela.mainloop()