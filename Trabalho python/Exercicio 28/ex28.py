import tkinter as tk
janela = tk.Tk()
janela.title("Calculadora Simples")
entrada1 = tk.Entry(janela)
entrada1.pack()
entrada2 = tk.Entry(janela)
entrada2.pack()
mensagem = tk.Label(janela, text="")
mensagem.pack()
def somar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    mensagem.config(text=f"Resultado: {resultado}")
def subtrair():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 - num2
    mensagem.config(text=f"Resultado: {resultado}")
def multiplicar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 * num2
    mensagem.config(text=f"Resultado: {resultado}")
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    if num2 != 0:
        resultado = num1 / num2
        mensagem.config(text=f"Resultado: {resultado}")
    else:
        mensagem.config(text="Erro: Divisão por zero!")

botao = tk.Button(janela, text="Somar", command=somar)
botao.pack()

botao = tk.Button(janela, text="Subtrair", command=subtrair)
botao.pack()

botao = tk.Button(janela, text="Multiplicar", command=multiplicar)
botao.pack()

botao = tk.Button(janela, text="Dividir", command=dividir)
botao.pack()

janela.mainloop()