"""
Zip - Unindo iteráveis  # Itera apenas quando tem quantidades iguais. Parando no que tem menor tamanho.
Zip_longest - Intertools  # Itera tudo. Considerando o que não tem como 'None'
"""
import itertools

indice = itertools.count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Florianópolis', 'Monte Belo']
estados = ['SP', 'MG', 'BA', 'SC']

cidades_estados = zip(indice, cidades, estados)  # cria um iterador;
# # for valor in cidades_estados:
# #     print(valor)
# # OU
# print(list(cidades_estados))

# cidades_estados = itertools.zip_longest(estados, cidades, fillvalue='Estado')  # preenche o que não tem com o que está
                                                                               # com nome entre ''
for indice, cidades, estados in cidades_estados:
    print(f'{indice} - {cidades} - {estados}')
