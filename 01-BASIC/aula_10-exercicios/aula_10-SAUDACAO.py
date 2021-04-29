"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Exemplo:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Digite o horário (0 - 23): ')

if hora.isdigit()
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('O horario de estar entre 0 e 23.')
    else:
        if (hora >= 0) and (hora <= 11):
            print('Bom dia.')
        elif (hora >= 12) and (hora <= 17):
            print('Boa tarde.')
        else:
            print('Boa noite.')
else:
    print('Não é um horário válido.')
