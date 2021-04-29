l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [variavel for variavel in l1]  # cria uma cópia idêntica a l1
print(ex1)
ex2 = [v * 2 for v in l1]  # multiplica o valor de v por 2
print(ex2)
ex3 = [(v, v2) for v in l1 for v2 in range(3)]  # cria uma lista de coordenadas (0, 1), (0, 2)...
print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]  # troca o a por @ dentro de toda a lista.
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]  # inverte as posições de X e Y
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # v recebe v dentro de l3 se for divisível por 3 e por 8
print(ex6)

ex7 = [v if v % 3 == 0 else 'Não é' for v in l3]  # para utilizar o else, precisa usar o if no começo
print(ex7)
ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]  # o AND precisa ser incluso caso tenha mais uma condição.
print(ex8)
