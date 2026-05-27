import tkinter as tk
janela = tk.Tk()
janela.title("Seletor de Cores")
cor_selecionada = tk.StringVar()
def selecionar_cor():
    janela.config(bg=cor_selecionada.get())
tk.Radiobutton(janela, text= "vermelho", variable=cor_selecionada, value="red", command=selecionar_cor).pack()
tk.Radiobutton(janela, text= "verde", variable=cor_selecionada, value="green", command=selecionar_cor).pack()
tk.Radiobutton(janela, text= "azul", variable=cor_selecionada, value="blue", command=selecionar_cor).pack()
janela.mainloop()
