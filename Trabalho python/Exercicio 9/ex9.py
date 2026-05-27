import re
def mascarar_cpf(texto):
    padrao = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    return re.sub(padrao, "XXX.XXX.XXX-XX", texto)
texto= "Meu CPF é 123.456.789-00 e o do meu amigo é 987.654.321-11."
print (mascarar_cpf(texto))