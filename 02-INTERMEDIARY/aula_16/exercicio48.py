def saudacao():
    nome = input('Como se chama? ')
    print(f'Olá, {nome}.')

saudacao()

def soma():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    resultado = n1 + n2 + n3
    print(f'A soma desses números é {resultado}.')
soma()
print()

def soma_percentual():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Qual percentual deseja acrescentar ao número? '))
    return n1 + (n1 * n2 / 100)

print(soma_percentual())

def fizzbuzz():
    n = int(input('Digite um número: '))

    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5.'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3.'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5.'
    return n

# from random import randint
#
# for i in range(100):
#     aleatorio = randint(0, 100)
#     print(fizzbuzz(aleatorio))
