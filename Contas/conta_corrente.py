from Contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, num, cliente, saldo_inicial = 0, limite = 100):
        super().__init__(num, cliente, saldo_inicial)
        self.__limite = limite

    def sacar(self, valor):
        saldo = self.get_saldo() + self.__limite

        if 0 < valor <= saldo:
            super().sacar(valor)  
        else:
            print("Saldo e limite insuficientes.")