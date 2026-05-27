import json
with open("Exercicio 5.6/produtos.json", "r") as arquivo:
    dados=json.load(arquivo)
    total = 0
    for produto in dados:
        valor = produto["preco"] * produto["estoque"]
        total += valor
print(f"O valor total do estoque é: R${total:.2f}")