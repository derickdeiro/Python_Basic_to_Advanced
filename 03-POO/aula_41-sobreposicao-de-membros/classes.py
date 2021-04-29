class Pessoa:  # SUPERCLASSE  (mãe) NÃO HERDA nada.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando na SUPER Classe...')


class Cliente(Pessoa):  # SUBCLASSE  (filha) HERDA o que é da Superclasse - CLASS ESPECÍFICA
    def comprar(self):
        print(f'{self.nomeclasse} comprando.')

    def falar(self):
        print(f'Estou em CLIENTE.')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):  # Inclui um atributo (sobrenome) e precisa
        Pessoa.__init__(self, nome, idade)  # puxar os atributos da Super Classe
        self.sobrenome = sobrenome

    def falar(self):  # sobrescrevendo o MÉTODO. A função de "Pessoa" não será mais executada aqui.
        super().falar()  # busca na Classe superior imediata o método específico, até encontrar.
        Pessoa.falar(self)  # busca na Classe específica
        print(f'{self.nome} {self.sobrenome}')
