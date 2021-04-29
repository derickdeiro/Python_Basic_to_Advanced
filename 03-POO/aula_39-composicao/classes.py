class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []  # lista para receber os endereços do cliente

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # associa a Class Endereço dentro desse atributo

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):  # PYTHON GARBAGE COLLECTOR. APAGA APOS UTILIZAÇÃO
        print(f'\033[31m{self.nome} FOI APAGADO\033[m')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'\033[31m{self.cidade}/{self.estado} FOI APAGADO\033[m')
