def gerar_iniciais(nome):
    palavras= nome.split()
    iniciais= ""
    for palavra in palavras:
        if (len(palavra)) > 2:
            iniciais += palavra[0].upper() + "."
    return iniciais
print(gerar_iniciais("Naytan de Oliveira"))