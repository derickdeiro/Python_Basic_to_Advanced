"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas  e um banco.
A ideia é que o cliente tenha uma conta (corrente ou poupança) e que possa sacar/depositar
nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas.

Dicas:
Criar classe Cliente que herda da Classe Pessoa (herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo -
    as subcasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Chegar se o cliente é daquele banco
    * Chegar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from cadastro import Banco, Cliente
from banco.conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)
banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)


cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(800)
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente2):
    cliente2.conta.sacar(100)
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(150)
else:
    print('Cliente não autenticado')

