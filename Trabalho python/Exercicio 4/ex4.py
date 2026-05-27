with open ("Exercicio 4/sistema.log", "r") as arquivo:
    linhas = arquivo.read()
    ERROR = linhas.count("ERROR")
    WARNING= linhas.count("WARNING")
    print(f"O arquivo tem {ERROR} erros.")
    print(f"O arquivo tem {WARNING} avisos.")