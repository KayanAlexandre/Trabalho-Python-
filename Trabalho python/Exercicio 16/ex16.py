def dividir():
    print(f"Digite dois números:")
    try:
        numero1= float(input("Digite um número: "))
        numero2= float(input("Digite outro número: "))
        resultado= numero1/numero2
        print(f" O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    except ValueError:
        print("Erro, digite um numero válido")
dividir()