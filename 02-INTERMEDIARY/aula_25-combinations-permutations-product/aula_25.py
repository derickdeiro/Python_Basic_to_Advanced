"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos.
Produto - Ordem importa e repete valores únicos
"""

import itertools
pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
for grupo in itertools.combinations(pessoa, 2):  # faz combinações de valores em X valor (valor, x)
    print(grupo)
print('~'*45)
for grupo in itertools.permutations(pessoa, 2):  # repete os valores iguais. (André, Luiz) == (Luiz, André)
    print(grupo)
print('~'*45)
for grupo in itertools.product(pessoa, repeat=2):  # repete o valor com ele mesmo.
    print(grupo)
