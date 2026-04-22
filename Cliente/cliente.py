class Cliente:
    def __init__(self, nome, cpf, end):
        self.__nome = nome
        self.__cpf = cpf
        self.__end = end

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_end(self):
        return self.__end

    def mostrar_dados(self):
        print(f"Cliente: {self.__nome} - CPF: {self.__cpf} - Endereço: {self.__end}")