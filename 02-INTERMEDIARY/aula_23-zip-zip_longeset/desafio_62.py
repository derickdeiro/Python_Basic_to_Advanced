import random
import itertools
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se a lista for maior que a outra, a soma só vai considerar o tamanho da menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
======== Resultado
lista_soma = [2, 4, 6, 8]
"""

lista_a = [random.randint(1, 100) for i in range(random.randint(1, 10))]
lista_b = [random.randint(1, 100) for i in range(random.randint(1, 10))]
print(lista_a)
print(lista_b)

lista_soma1 = [(x+y) for x, y in zip(lista_a, lista_b)]  # somando até o len da menor lista
print(lista_soma1)

lista_soma2 = [x + y for x, y in itertools.zip_longest(lista_a, lista_b, fillvalue=0)]  # substitui o restante do len
                                                                                        # da menor por 0
print(lista_soma2)