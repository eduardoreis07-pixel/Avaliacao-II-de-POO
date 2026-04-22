from Historico.historico import Historico

class Conta:
    def __init__(self, num, cliente, saldo_inicial = 0):
        self.__num = num
        self.__cliente = cliente
        self.__saldo = saldo_inicial
        self.__historico = Historico()


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.add_operacao("Deposito", valor)
            print("\nDepósito realizado.\n")
        else:
            print("\nDepósito inválido.\n")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.add_operacao("Saque", valor)
            print("\nSaque realizado.\n")
        else:
            print("\nSaldo inválido.\n")

    def get_saldo(self):
        return self.__saldo
    
    def show_historico(self):
        self.__historico.list()

    def get_num(self):
        return self.__num

    def get_cliente(self):
        return self.__cliente