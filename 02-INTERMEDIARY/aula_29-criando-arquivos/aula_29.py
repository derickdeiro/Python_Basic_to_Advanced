file = open('abc.text', 'w+')  # w+ LIMPA o arquivo e escreve novamente. Leitura e escrita
file.write('Linha 1\n')  # escreve linhas no arquivo
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # volta o cursor do arquivo para a posição selecionada (0 == topo)
print('Lendo Linhas:')
print(file.read())  # lê o arquivo inteiro

print('~'*45)

file.seek(0, 0)
print(file.readline(), end='')  # lê linha por linha do arquivo e quebra ela.

print('~'*45)
file.seek(0, 0)
print(file.readlines(), end='')  # lê em formato de lista

print()
print('~'*45)
file.seek(0, 0)
for linha in file.readlines():  # Lê linha por linha
    print(linha, end='')


file.close()  # SEMPRE fechar o arquivo