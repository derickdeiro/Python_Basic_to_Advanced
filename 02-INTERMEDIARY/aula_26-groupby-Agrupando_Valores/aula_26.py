import itertools
alunos = [
    {'nome': 'Derick', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Karla', 'nota': 'A'},
    {'nome': 'Clara', 'nota': 'C'},
    {'nome': 'Stheffany', 'nota': 'B'},
    {'nome': 'Filipe', 'nota': 'D'},
    {'nome': 'Pedro', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'José', 'nota': 'D'},
    {'nome': 'Fernando', 'nota': 'A'},
]

ordena = lambda item: item['nota']  # uma "função" para ordenar
alunos.sort(key=ordena)
# for i in alunos:
#     print(i)
alunos_agrupados = itertools.groupby(alunos, ordena)  # agrupa itens que são iguais. Nesse caso a Key "Nota"

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = itertools.tee(valores_agrupados)  # cria duas cópias do iterador (va1 e va2)
    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno["nome"]}')

    quantidade = len(list(va2))
    print(f'{quantidade} tiraram nota {agrupamento}')
    print()
