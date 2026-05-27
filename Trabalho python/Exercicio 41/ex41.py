import tkinter as tk
from tkinter import filedialog
import re
import json
janela = tk.Tk()
janela.title("Visualizador de logs")
texto = tk.Text(janela)
texto.pack()
logs_criticos = []
def carregar_arquivo():
    arquivo= filedialog.askopenfilename(filetypes=[("Arquivos de Log", "*.log")])
    with open (arquivo, "r") as file:
        texto.delete("1.0", "end")
        for linha in file:
            if re.search(r"\[CRITICAL\]", linha):
                logs_criticos.append(linha.strip())
                texto.insert(tk.END, linha)
def exportar_json():
                    with open("logs_criticos.json", "w") as json_file:
                        json.dump(logs_criticos, json_file, indent=4)
botao_carregar = tk.Button(janela, text="Carregar Log", command=carregar_arquivo)
botao_carregar.pack()
botao_exportar = tk.Button(janela, text="Exportar JSON", command=exportar_json)
botao_exportar.pack()
janela.mainloop()
