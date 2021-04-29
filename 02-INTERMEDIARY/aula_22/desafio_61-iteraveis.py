carrinho = []

carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 30))
carrinho.append(('Produto 3', 50))

print(carrinho)
total = [(produto, preco) for produto, preco in carrinho]  # Desempacota o que tem em carrinho para total
print(total)
total = [preco for produto, preco in carrinho]  # Desempacota somente o preco para o total
print(total)
total = [float(preco) for produto, preco in carrinho]  # converte o preço para número real
print(total)
# RESOLUÇÃO FINAL
total = sum([float(preco) for produto, preco in carrinho])  # soma os valores dentro de total
print(total)


