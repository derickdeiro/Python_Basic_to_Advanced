"""
Faça um programa que paça para o primeiro nome do usuário. Se o nome tiver menos de 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande')