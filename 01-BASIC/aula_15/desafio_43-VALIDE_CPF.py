"""
VALIDE UM CPF
"""

cpf = input('Digite seu CPF (apenas números): ')
cpf_int = []
novocpf = cpf_int[:-2]
lista = list(range(10, 1, -1))
resultado = []
resultado2 = []

while not cpf.isdigit():
    print('Dados incorretos. Tente novamente.')

    cpf = input('Digite seu CPF (apenas números): ')

    print()

    for val in cpf:
        cpf_int.append(int(val))

    for i in resultado:
        resultado.append(novocpf[i] * lista[i])

    soma = 0
    for i in resultado:
        soma = soma + i

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    if digito1 == cpf_int[9]:
        lista.insert(11)
    else:
        print('CPF INVÁLIDO!')

    cpf_int.append(digito1)

    # for i in resultado2:
    #     resultado2.append(cpf_int[i] * lista[i])

    soma = 0
    for i in resultado2:
        soma = soma + i
    digito2 = 11 - (soma % 11)

    if digito1 == cpf_int[9] and digito2 == cpf_int[10]:
        print('Seu CPF é válido.')
    else:
        print('CPF inválido.')
