def valida(cnpj):
    cnpj = remove_especiais(cnpj)

    try:
        if sequencial(cnpj):
            return False
    except:
        return False
    try:
        novocnpj = calcula_digito(cnpj, digito=1)
        novocnpj = calcula_digito(novocnpj, digito=2)
    except Exception:
        return False

    if novocnpj == cnpj:
        return True
    else:
        return False


def remove_especiais(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def sequencial(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        contador = 5
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        contador = 6
        novo_cnpj = cnpj
    else:
        return False
    total = 0
    for x in novo_cnpj:
        if contador < 2:
            contador = 9
        total += int(x) * contador
        contador -= 1
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f'{novo_cnpj}{digito}'


def gera_cnpj():
    from random import randint
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = '0001'
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'
    novo_cnpj = calcula_digito(inicio_cnpj, digito=1)
    novo_cnpj = calcula_digito(novo_cnpj, digito=2)
    return novo_cnpj


def formata(cnpj):
    cnpj = remove_especiais(cnpj)
    formatado = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    return formatado


for i in range(10):
    cnpj = gera_cnpj()
    formatado = formata(cnpj)
    if valida(formatado):
        print(f'O CNPJ {formatado} é válido')
    else:
        print(f'O CNPJ {formatado} é inválido')
