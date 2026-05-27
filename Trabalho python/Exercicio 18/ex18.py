nome= input("Digite o nome do arquivo: ")
try:
    with open(nome, "r") as arquivo:
        texto= arquivo.read()
        print(texto)
except FileNotFoundError:
        print(f"O arquivo '{nome}' não foi encontrado.")
except PermissionError:
        print(f"Você não tem permissão para ler o arquivo '{nome}'.")