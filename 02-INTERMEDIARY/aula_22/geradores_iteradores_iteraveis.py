import sys

# lista = list(range(100))
# print(sys.getsizeof(lista))  # mostra o quanto de memória consome essa lista.

l1 = [x for x in range(100)]  # lista
# def geralista():
#     r1 = []
#     for n in range(100):
#         r1.append(n)
#     return r1


l2 = (x for x in range(100))  # gerador
# outra forma de criar um gerador
# def geralista():
#     for n in range(100):
#         yield n

print(f'{l1}')
print(f'Ocupa na memória {sys.getsizeof(l1)} bytes')
print(f'É do tipo {type(l1)}')

print(f'Não é possível imprimir assim: {l2} Somente igual abaixo:')
for v in l2:
    print(f'{v}, ', end='')
print()
print(f'Ocupa na memória {sys.getsizeof(l2)} bytes')  # GERADORES OCULPAM MENOS ESPAÇO NA MEMÓRIA
print(f'É do tipo {type(l2)}')
