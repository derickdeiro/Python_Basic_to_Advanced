"""
O módulo Dataclasses fornece um decorador e funções para cirar automaticamente métodos, como
__init__(), __repr__(), __eq__ (etc)
"""

from dataclasses import dataclass, asdict


# é um facilitador.
@dataclass(order=True)  # permite ordernar
class Pessoa:
    nome: str  # não precisa incluir o self.nome = nome
    sobrenome: str

    @property  # transforma o método em Getter e não precisa usar o () ao final
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Derick', 'Deiró')
p2 = Pessoa('Karla', 'Azevedo')
p3 = Pessoa('Fernando', 'Bezerra')
p4 = Pessoa('Filipe', 'Silva')
p5 = Pessoa('Clara', 'Moura')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas))
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))

print(asdict(p2))  # transforma em dicionário.

# print(f'{p1.nome}')
# print(f'{p1.sobrenome}')
# print(p1.nome_completo)
