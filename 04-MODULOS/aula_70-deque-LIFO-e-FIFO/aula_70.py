"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exmeplo: Pilha de livros que são adicionados um sobre o outro.
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
"""
from collections import deque
from time import sleep

# LIFO
livros = list()
livros.append('Livro1')  # 1
livros.append('Livro2')  # 2
livros.append('Livro3')  # 3
livros.append('Livro4')  # 4
livros.append('Livro5')  # 5
livro_removido = livros.pop()  # 5
livro_removido = livros.pop()  # 4
livro_removido = livros.pop()  # 3

print(f'Livros na pilha: {livros} - Livro na mão: {livro_removido}')

fila = deque()
fila.append('Derick')
fila.append('Karla')
fila.append('Marcos')
fila.append('José')
print(f'Saiu: {fila.popleft()}')  # sai o primeiro elemento da lista
print(f'Saiu: {fila.popleft()}')  # sai o primeiro elemento da lista

for nome in fila:
    print(nome)


# FIFO
fila = deque(maxlen=5)  # tamanho máximo da lista

for i in range(20):
    fila.append(i)
    sleep(1)
    print(fila)  # o último valor é adicionado e o primeiro é removido até restar o tamanho da lista.
