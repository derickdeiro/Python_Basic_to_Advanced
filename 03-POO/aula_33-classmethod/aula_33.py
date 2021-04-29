from datetime import date


class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # METODO DE CLASSE ao invés de METODO DE INSTANCIA
    def por_ano_nascimento(cls, nome, ano_nascimento):  # por convenção, é utilizado "cls" como "Class"
        idade = cls.ano_atual - ano_nascimento  # uma variável que está disponível apenas nessa função
        return cls(nome, idade)  # retorna a própria classe com os atributos


p1 = Pessoa.por_ano_nascimento('Luiz', 1991)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()  # define o ano de nascimento.
