def contar(texto):
    vogais= 0
    consoantes= 0
    texto= texto.lower()
    for letra in texto:
        if letra in "aeiou":
            vogais += 1
        elif letra.isalpha():
            consoantes += 1
    return vogais, consoantes
print (contar("Meu nome é naytan e faço python"))