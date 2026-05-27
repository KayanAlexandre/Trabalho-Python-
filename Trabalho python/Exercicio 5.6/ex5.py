produtos=[ {"nome": "Mouse", "id": 1, "estoque": 10,"preco": 20.00},
    {"nome": "Teclado", "id": 2, "estoque": 5,"preco": 50.00},
    {"nome": "Monitor", "id": 3, "estoque": 2,"preco": 200.00},
    {"nome": "computador", "id": 4, "estoque": 1,"preco": 1500.00},
    {"nome": "Cadeira", "id": 5, "estoque": 3,"preco": 100.00}
]
import json
with open("Exercicio 5.6/produtos.json", "w") as arquivo:
    json.dump(produtos, arquivo, indent=4)