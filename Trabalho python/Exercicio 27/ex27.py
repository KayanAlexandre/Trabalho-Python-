import tkinter as tk
janela = tk.Tk()
janela.title("Boas Vindas")
entrada = tk.Entry(janela)
entrada.pack()
mensagem = tk.Label(janela, text="")
mensagem.pack()
def click():
    nome = entrada.get()
    mensagem.config(text=f"Olá, {nome}!")
botao = tk.Button(janela, text="Click", command=click)
botao.pack()
janela.mainloop()    
