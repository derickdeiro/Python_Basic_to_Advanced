import math

PI = math.pi  # cria uma variável com o cálculo de pi


def dobraLista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == '__main__':  # executa apenas o principal
    lista = [1, 2, 3, 4, 5]
    print(dobraLista(lista))
    print(multiplica(lista))
    print(PI)
