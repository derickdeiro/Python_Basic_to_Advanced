
print()
print('TEXTO EXPLICATIVO:')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*3? ',
        'respostas': {'a': '7', 'b': '9', 'c': '6'},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 7*9? ',
        'respostas': {'a': '63', 'b': '52', 'c': '79'},
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 14+7? ',
        'respostas': {'a': '27', 'b': '21', 'c': '32'},
        'resposta_certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8*6? ',
        'respostas': {'a': '64', 'b': '40', 'c': '48'},
        'resposta_certa': 'c'
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Qual é sua resposta? ')

    if resposta_usuario == pv['resposta_certa']:
        print('Oba! Você acertou.')
        respostas_certas += 1
    else:
        print('ERRRRROOOOOUUUUU!!!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

if respostas_certas > 1:
    plural = 'perguntas'
else:
    plural = 'respostas'
print(f'Você acertou {respostas_certas} {plural}.')
print(f'Seu aproveitamento foi de {porcentagem_acerto}%.')
