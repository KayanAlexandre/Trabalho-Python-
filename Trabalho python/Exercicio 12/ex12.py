import re
texto ="Ana"
def eh_palidromo(texto):
    limpar= re.sub(r"[^a-z0-9]", "", texto.lower())
    invertido= limpar[::-1]
    return limpar==invertido
print(eh_palidromo(texto))