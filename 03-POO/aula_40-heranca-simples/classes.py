class Pessoa:  # SUPERCLASSE  (mãe) NÃO HERDA nada.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):  # SUBCLASSE  (filha) HERDA o que é da Superclasse - CLASS ESPECÍFICA
    def comprar(self):
        print(f'{self.nomeclasse} comprando.')


class Aluno(Pessoa):  # SUBCLASSE (filha) HERDA o que é da Superclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando.')
