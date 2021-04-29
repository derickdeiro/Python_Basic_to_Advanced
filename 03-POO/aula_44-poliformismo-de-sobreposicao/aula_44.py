"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais
(de mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros.
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass  # ele não tem nada, então só passa.


class B(A):
    def fala(self, msg):  # mesma assinatura que A
        print(f'B está falando sobre {msg}')  # polimorfismo está trocando a frase.


class C(A):
    def fala(self, msg):
        print(f'C está falando sobre {msg}')


b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro Assunto')
