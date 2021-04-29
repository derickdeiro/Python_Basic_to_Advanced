class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    @idade.setter
    def idade(self, valor):
        self._idade = int(valor)


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
