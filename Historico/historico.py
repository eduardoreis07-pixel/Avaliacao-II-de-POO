class Historico:
    def __init__(self):
        self._operacoes = []

    def add_operacao(self, tipo, valor):
        self._operacoes.append(f"{tipo} de R$ {valor}")

    def list(self):
        for op in self._operacoes:
            print(op)