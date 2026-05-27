import re
with open('Exercicio 31/ex31.txt', 'r') as file:
    texto = file.read()
padrao = r"\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}"
datas = re.findall(padrao, texto)
for data in datas:
        if "/" in data:
            dia, mes, ano = data.split("/")
            nova_data = f"{dia}-{mes}-{ano}"
        elif "-" in data:
            ano, mes, dia = data.split("-")
            nova_data = f"{dia}-{mes}-{ano}"
        texto = texto.replace(data, nova_data)
with open('Exercicio 31/novo_arquivo.txt', 'w') as file:
        file.write(texto)
print("arquivo criado com sucesso")