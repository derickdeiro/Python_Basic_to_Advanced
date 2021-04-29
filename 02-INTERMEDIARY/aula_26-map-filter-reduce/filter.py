from dados import produtos, lista, pessoas

# filter é semelhante ao map. Retornando apenas True ou False. Mantendo o True e removendo o False
novalista = filter(lambda x: x>5, lista)
# novalista = [x for x in lista if x > 5]  # mesma forma que o filter

for i in lista:
    print(f'{i} ', end='')
print()
for i in novalista:
    print(f'{i} ', end='')
print()

maiorproduto = filter(lambda p: p['preco'] > 50, produtos)

for preco in maiorproduto:
    print(preco)

print('~'*45)
def filtra(pessoa):
    if pessoa['idade'] > 30:
        return True
    else:
        return False


# maior_idade = filter(filtra, pessoas)
maior_idade = filter(lambda p: p['idade'] > 30, pessoas)

for pessoa in maior_idade:
    print(pessoa)
