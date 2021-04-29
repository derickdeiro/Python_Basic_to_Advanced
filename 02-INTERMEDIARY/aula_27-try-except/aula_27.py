def converte_numero(valor):  # recebe uma STR
    try:
        valor = int(valor)  # tenta converter em um número inteiro
        return valor        # se der certo, retorna o valor como Tnteiro
    except ValueError:      # se der errado
        try:
            valor = float(valor)  # tenta converter em número real
            return valor          # se der certo, retorna o valor como Float
        except ValueError:
            pass                  # se der erro, retorna como None, pois não está declarado o retorno.


while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Erro! Digite um número válido.')
    else:
        print(f'{numero} x 2 = {numero * 2}')
        break
