from datetime import date
from random import randint


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
        return cls(nome, idade)

    # decorador ESTATICO. Não precisa ser ligado à instância e nem a Classe
    @staticmethod  # não pode utilizar "self" e nem "cls"
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Derick', 29)
print(Pessoa.gera_id())
print(p1.gera_id())
