import re
texto =" O meu numero é (21) 98263-9234"
padrao= r"\(\d{2}\) 9\d{4}-\d{4}"
telefone= re.findall(padrao, texto)
print (telefone)