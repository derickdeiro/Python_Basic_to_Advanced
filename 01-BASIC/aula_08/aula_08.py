'''
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

nome = 'Derick'
idade = 29
altura = 1.73
peso = 73.5
ano = 2020
imc = peso / altura ** 2
nascimento = ano - idade

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}KG.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
