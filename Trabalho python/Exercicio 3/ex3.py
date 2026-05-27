import csv

with open("Exercicio 3/funcionarios.csv", "r") as leitura, \
     open("Exercicio 3/funcionarios_filtrados.csv", "w", newline="") as escrita:
    leitor = csv.DictReader(leitura)
    dictwriter = csv.DictWriter(
        escrita,
        fieldnames=["Nome", "Cargo", "Salario"]
    )
    dictwriter.writeheader()
    for linha in leitor:
        salario = int(linha["Salario"])
        if salario > 5000:
            dictwriter.writerow(linha)
            print(linha)