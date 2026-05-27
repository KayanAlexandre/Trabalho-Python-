with open ("Exercicio 2/dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    linhas_invertidas = linhas[::-1]
    texto = "".join(linhas_invertidas)
    with open("Exercicio 2/dados_invertidos.txt", "w") as arquivo:
        arquivo.write(texto) 