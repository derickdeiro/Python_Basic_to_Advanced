# TENTATIVA JOGO ADIVINHACAO

secreto = 'perfume'
digitadas = []
erradas = []
chance = 3

while True:
    letra = input('Digite uma letra: ')

    if chance <= 0:
        print('Suas chances acabaram... Você perdeu =(')
        break

    if len(letra) > 1:
        print('Opa, isso não vale. Digite apenas uma letra.')
        continue

    digitadas.append(letra)
    erradas.append(letra.upper())

    if letra in secreto:
        print(f'Eba! A letra {letra} existe na palavra secreta.')
        erradas.pop()
    else:
        print(f'Que pena... A letra {letra} NÃO EXISTE na palavra secreta. Tente outra.')
        digitadas.pop()

    print('Existentes:', digitadas)
    print('ERRADAS:', erradas)

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Uhhuuuulll! Você venceu. A palavra secreta é {secreto}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chance -= 1

    print(f'Você ainda tem {chance} chances.')
    print()
