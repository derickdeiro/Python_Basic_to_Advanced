from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor precisa ser numérico')

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: R$ {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=150):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            print(f'Saldo Insuficiente.')
            return

        self._saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print(f'Saldo insuficiente')
            return
        self._saldo -= valor
        self.detalhes()
