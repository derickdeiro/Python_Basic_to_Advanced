from dados import lista, pessoas, produtos
from functools import reduce

# a função REDUCE faz a mesma coisa que o código abaixo.
acumula = 0
for valor in lista:
    acumula += valor
print(acumula)

# ac = acumulador, i de item. RECEBE (:) i + acumulador na lista começando em 0.
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade)
media = soma_idade/len(pessoas)
print(media)
