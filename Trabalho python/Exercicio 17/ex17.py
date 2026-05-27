lista= [12, "23", 45, "ab", "67", 89,[2, 3]]
for item in lista:
    try:
        convertido = float(item)
        print(f"O número {convertido} é um número válido.")
    except ValueError:
        print(f"O item '{item}' não é um número válido.")
    except TypeError:
        print(f"O item '{item}' não é um número válido.")