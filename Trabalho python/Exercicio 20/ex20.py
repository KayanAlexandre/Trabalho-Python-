import random
class ConnectionTimeoutError(Exception):
    pass
def requisicao():                       
    numero= random.randint(1,10)
    print(f"Número gerado: {numero}")
    if numero %2 == 0:
        raise ConnectionTimeoutError("Timeout da conexão.")
try:
        requisicao()
except ConnectionTimeoutError:
        print(f"Erro: A requisição excedeu o tempo limite.")
