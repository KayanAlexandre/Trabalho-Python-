with open("Exercicio 1/poema.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    texto = "".join(linhas)
    palavras = texto.split()
    print(f"O poema tem {len(palavras)} palavras.")
    total_de_linhas = len(linhas)
    print(f"O poema tem {total_de_linhas} linhas.")
