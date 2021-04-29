"""
Comma Separated Values - CSV (valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados, clientes de email, etc.
"""

import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)  # variável para ler o arquivo em formato csv.
    # dados = csv.DictReader(arquivo)  # lê em formato de dicionário
    dados = [x for x in csv.DictReader(arquivo)]  # converter em lista com listcomprehension

    # for dado in dados:
        # print(dado)
        # print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

with open('clientes2.csv', 'w') as arquivo:  # criando um novo TXT
    escreve = csv.writer(
        arquivo,  # é o próprio arquivo que será gerado.
        delimiter=',',  # delimitador para separação é a vírgula
        quotechar='"',  # qual caracter é utilizado para colocar aspas
        quoting=csv.QUOTE_ALL  # todos os valores estarão entre aspas
    )

    chaves = dados[0].keys()  # para incluir o índice de colunas ao topo
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )