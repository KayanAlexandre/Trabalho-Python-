import re
def validar_senha(senha):
    padrao = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(padrao, senha):
        return True
    else:
        return False
print(validar_senha("join@1234"))