class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None  # esse atributo recebe uma das classes através da Associação

    @property
    def nome(self):  # getter
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print(f'Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está digitando...')
