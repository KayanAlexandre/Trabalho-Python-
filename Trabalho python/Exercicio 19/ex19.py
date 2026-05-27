lista = ["agua","fogo","ar","terra", "raio"]
try:
    indice= int(input("Digite um índice para acessar o elemento da lista: "))
    print(lista[indice])
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")