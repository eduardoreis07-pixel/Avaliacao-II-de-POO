class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = []

    def add_conta(self, conta):
        self._contas.append(conta)
        print("\nConta adicionada.\n")

    def search_conta(self, num):
        for conta in self._contas:
            if conta.get_num() == num:
                return conta
        return None