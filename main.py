from Banco.banco import Banco
from Cliente.cliente import Cliente

from Contas.conta_corrente import ContaCorrente
from Contas.conta_poupanca import ContaPoupanca

def menu():
    print("1 - Nova conta")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Saldo")
    print("5 - Histórico")
    print("6 - Sair")


if __name__ == "__main__":
    banco = Banco("Banco Banco")

    while True:
        menu()
        x = input("\n")

        if x == "1":
            print("\n\nNova Conta")

            num = int(input("Número da conta: "))
            conta = banco.search_conta(num)

            if conta is not None:
                print("\nConta inválida.\n")
                continue

            else:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                end = input("Endereço: ")

                cliente = Cliente(nome, cpf, end)

                tipo = input("Conta (1 - Corrente; 2 - Poupança): ")
                if tipo == "1":
                    limite = float(input("Limite: "))
                    conta = ContaCorrente(num, cliente, 0, limite)
                elif tipo == "2":
                    conta = ContaPoupanca(num, cliente, 0)
                else:
                    print("\nInválido.\n")
                    continue

                banco.add_conta(conta)
                print("\nConta criada.\n")

        elif x == "2":
            print("\n\nDepósito")
            num = int(input("Número da conta: "))
            conta = banco.search_conta(num)

            if conta is None:
                print("\nConta inválida.\n")
            else:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)

        elif x == "3":
            print("\n\nSaque")
            num = int(input("Número da conta: "))
            conta = banco.search_conta(num)

            if conta is None:
                print("\nConta inválida.\n")
            else:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)

        elif x == "4":
            print("\n\nSaldo")
            num = int(input("Número da conta: "))
            conta = banco.search_conta(num)

            if conta is None:
                print("\nConta inválida.\n")
            else:
                print("\nSaldo:", conta.get_saldo(), "\n")

        elif x == "5":
            print("\n\nHistórico")
            num = int(input("Número da conta: "))
            conta = banco.search_conta(num)

            if conta is None:
                print("\nConta inválida.\n")
            else:
                print("\n")
                conta.show_historico()
                print("\n")

        elif x == "6":
            break

        else:
            print("\n")