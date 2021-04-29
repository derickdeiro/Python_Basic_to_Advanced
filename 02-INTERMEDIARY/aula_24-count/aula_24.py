"""
count - Itertools
"""
from itertools import count

# contador = count()  # dessa forma o count não tem fim.
contador_num = count(start=5, step=-1)  # começa em X e pula de Y em Y
                                      # para contar para trás deve ser -1
for valor in contador_num:  # entrará em looping infinito e poderá travar o PC
    print(round(valor, 2))  # arredonda o número real com duas casas decimais.

    if valor >= 10 or valor <= -10:
        break

contador = count()
lista = ['Luiz', 'João', 'Maria', 'José', 'Silva', 'Eduardo', 'Derick']
lista = zip(contador, lista)
print(list(lista))
