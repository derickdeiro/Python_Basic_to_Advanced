class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # lista para juntar os produtos

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0  # para somar os valores.
        for produto in self.produtos:
            total += produto.valor  # para cada produto na lista, soma o valor ao total.
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor