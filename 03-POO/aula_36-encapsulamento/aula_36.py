"""
Método e atributo:
public (pode ser acessado dentro e fora da classe)
protected (acessado apenas dentro da classe ou das filhas da classe - herança)
private (disponível apenas dentro da classe)

# POR CONVEÇÃO É UTILIZADO DESSA FORMA PARA RECOMENDAR NÃO ALTERAR.

_ #protected  NÃO ALTERAR
__  #private  NÃO ALTERAR DE FORMA ALGUMA  (_NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):  # construtor
        self.__dados = {}  # Este é o coração da class, tudo acontece em volta dele.

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:  # se não existir essa chave, crie.
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})  # atualiza os dados.

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()
