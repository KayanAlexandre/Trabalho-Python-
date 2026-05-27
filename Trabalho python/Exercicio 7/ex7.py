import re
def validar_email(email):
    padrao = ".+@.+\..+"
    if re.match(padrao, email):
        return True
    else:
        return False
print(validar_email("naytan@gmail.com"))