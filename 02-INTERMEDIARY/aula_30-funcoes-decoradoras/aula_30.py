# DECORADORA
def master(funcao):  # função MASTER que recebe uma função
    def slave():     # função ESCRAVA que executa a função recebida
        print('Agora estou decorada')
        funcao
    return slave   # retorna a função executada sem o parâmetro


def fala_oi():
    print('Oi')

@master
def fala_oi2():
    print('Oi')


# fala_oi()
fala_oi2()

# FUNÇÃO ANINHADA
def velocidade(funcao):  # função MASTER que recebe uma função
    from time import time
    from time import sleep
    def interna(*args, **kwargs):  # função SLAVE desempacota args e kwargs
        star_time = time()  # variável que inicia o "cronômetro"
        resultado = funcao(*args, **kwargs)  # EXECUTA a função recebida na MASTER (sem os *args e **kwargs, pode dar erro
        end_time = time()  # variável que encerra o "cronômetro"
        tempo = (end_time - star_time) * 1000  # variável que encontra o tempo e converte para miléssimos de segundos
        print(f'\nA função "{funcao.__name__}" levou {tempo:.2f}ms para executar.')
        return resultado  # retorna a função
    return interna  # retorna a SLAVE sem pedir parâmetro

@velocidade
def demora():
    for i in range(100):
        print(i, end='')

demora()
