import re
padrao = r"^\d{1,3}(\.\d{1,3}){3}$"
while True:
        try:
            ip = input("Digite um endereço IP: ")
            if not re.match(padrao, ip):
                raise ValueError("Endereço IP inválido")
            print("Endereço IP válido")
            break
        except ValueError:
            print("Endereço IP inválido. Tente novamente.") 