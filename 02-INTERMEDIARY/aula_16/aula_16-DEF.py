def saudacao(msg='Olá', nome='usuário'):
    msg = 'Olá'
    nome = input('Como se chama? ')
    return f'{msg} {nome}.'

print(saudacao())

def divisao():
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro '))

    if n2 == 0:
        return

    return n1/n2

divide = divisao()

if divide:
    print(divide)
else:
    print('Conta inválida.')