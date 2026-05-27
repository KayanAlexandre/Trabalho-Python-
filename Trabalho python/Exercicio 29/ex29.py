import tkinter as tk
janela = tk.Tk()
janela.title("Contador")
contador = 0
def clicar():
    global contador
    contador += 1
    label.config(text= contador)
label = tk.Label(janela, text=contador)
label.pack()
botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack()
janela.mainloop()