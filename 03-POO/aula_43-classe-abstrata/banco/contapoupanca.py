from banco.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:  # se o saldo for menor que o valor de saque, ERRO.
            print('Saldo Insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
