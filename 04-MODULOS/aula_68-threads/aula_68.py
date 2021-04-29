from time import sleep
from threading import Thread  # executa o programa em paralelo a outras funções.


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()  # init do Thread

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)  # após 5seg o texto aparece.
t1.start()

t2 = MeuThread('Thread 2', 2)
t2.start()

t3 = MeuThread('Thread 3', 8)
t3.start()


for i in range(20):
    print(i)
    sleep(1)

