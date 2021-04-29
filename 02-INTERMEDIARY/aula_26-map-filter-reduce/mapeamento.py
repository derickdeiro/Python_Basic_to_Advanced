from dados import produtos, pessoas, lista

# Map sempre recebe o primeiro argumento como função. Passando por cada elemento da lista/dicionário
# Mapeamento recebe = p retorna p na key ['preco'] dentro da lista produtos
# lambda == list comprehension
precos = map(lambda p: p['preco'], produtos)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] + (p['preco']*5/100), 2)
    return p


# O lambda não consegue fazer um cálculo de aumento de preço, por exemplo. Por isso foi criada a função.
novos_produtos = map(aumenta_preco, produtos)

for preco in novos_produtos:
    print(preco)

print('~'*45)

def aumenta_idade(p):
    p['nova idade'] = round(p['idade'] * 1.20)  # aumenta a idade em 20%
    return p


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
