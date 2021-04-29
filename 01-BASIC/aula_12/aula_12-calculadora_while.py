while True:

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isdigit() or not num_2.isdigit():
        print('Digite um número válido.')
        continue

    else:
        num_1 = float(num_1)
        num_2 = float(num_2)

    operador = input('Digite a operadoração (+, -, /, *): ')

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Não é um operador válido.')

    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
    else:
        continue
