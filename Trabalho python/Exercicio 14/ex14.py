def inverter_texto(texto):
    nova= ""
    for letra in texto:
        if letra.isupper():
            nova += letra.lower()
        elif letra.islower():
            nova += letra.upper()
        else:
            nova += letra
    return nova
print(inverter_texto("Meu nome é Naytan e faço Python 123"))