import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
janela = tk.Tk()
janela.title("Criptografador de Arquivos")
arquivo_selecionado = ""
def selecionar_arquivo():
    global arquivo_selecionado
    arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    label_arquivo.config(text=arquivo_selecionado)
def criptografar():
    try:
        chave = int(entrada_chave.get())
        with open(arquivo_selecionado, "r", encoding="utf-8") as file:texto = file.read()
        texto_criptografado = ""
        for caractere in texto:
            novo_caractere = chr(ord(caractere) + chave)
            texto_criptografado += novo_caractere
        novo_arquivo = (arquivo_selecionado + ".enc")
        with open(novo_arquivo,"w",encoding="utf-8") as file:
            file.write(texto_criptografado)
        messagebox.showinfo( "Sucesso", "Arquivo criptografado!" )
    except ValueError:
        messagebox.showerror("Erro","Digite uma chave numérica!" )
    except FileNotFoundError:
        messagebox.showerror( "Erro","Selecione um arquivo!")
botao_arquivo = tk.Button(janela,text="Selecionar Arquivo",command=selecionar_arquivo)
botao_arquivo.pack()
label_arquivo = tk.Label(janela,text="Nenhum arquivo selecionado")
label_arquivo.pack()
tk.Label(janela,text="Chave Numérica").pack()
entrada_chave = tk.Entry(janela)
entrada_chave.pack()
botao_criptografar = tk.Button(janela,text="Criptografar",command=criptografar)
botao_criptografar.pack()
janela.mainloop()