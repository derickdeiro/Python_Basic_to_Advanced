class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter recebe o valor de preço antes de atribuir no __init__
    @property  # decorador de propriedade
    def preco(self):
        return self._preco  # por conveção é atribuido o nome do parâmetro com _ na frente

    # Setter Converte o valor recebido em algo para não dar erro.
    @preco.setter  # nome da propridade acompanhado por setter.
    def preco(self, valor):  # valor é o que será atribuido para a variável (preco da instancia __init__)
        if isinstance(valor, str):  # se a variável é uma instância do tipo XPTO
            valor = float(valor.replace('R$', ''))  # substitiu o R$ por nada

        self._preco = valor  # getter recebe "valor"


p1 = Produto('camiseta', 'R$53')
p2 = Produto('CANECA', 14.3)
print(p1.nome, p1.preco)
print(p2.nome, p2.preco)
p1.desconto(10)
print(p1.preco)


