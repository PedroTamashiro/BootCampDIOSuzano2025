class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario:      
    # TODO: Inicialize a lista de contas:
    def __init__(self):
        self._contas = []
    
    # TODO: Crie uma nova conta e adicione à lista de contas:
    def criar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        self._contas.append(conta)

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):
        string = ''
        for conta in self._contas:
            string += f'{conta._titular}: R$ {conta._saldo}, '
        string = string[:-2:]
        print(string)
        
#TODO: Crie uma instância de SistemaBancario:
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()