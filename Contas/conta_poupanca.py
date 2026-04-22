from Contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, num, cliente, saldo_inicial = 0):
        super().__init__(num, cliente, saldo_inicial)

    def sacar(self, valor):
        saldo = self.get_saldo() 

        if 0 < valor <= saldo:
            super().sacar(valor)  
        else:
            print("Saldo insuficiente.")