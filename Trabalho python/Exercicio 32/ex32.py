import csv
with open('Exercicio 32/vendas.csv', 'r') as arquivo:
    with open('Exercicio 32/log.txt', 'w') as log:
     linhas = arquivo.readlines()
     for linha in linhas:
        dados = linha.strip().split(',')
        try:
            valor = float(dados[1])
            print(f"valor valido {valor}")
        except ValueError:
            log.write(f"Valor inválido na linha: {linha}\n")
