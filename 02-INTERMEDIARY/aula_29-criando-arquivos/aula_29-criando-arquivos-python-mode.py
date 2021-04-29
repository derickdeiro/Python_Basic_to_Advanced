                                      # APAGA TUDO QUE TEM NO ARQUIVO
with open('abc.text', 'w+') as file:  # Variável recebe open e não tem a necessidade de fechar
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())


print('LENDO\n')

with open('abc.text', 'r') as file2:  # 'r' faz a leitura do arquivo
    print(file2.read())


with open('abc.text', 'a+') as file3:  # 'a+' coloca o cursor no final do arquivo e faz a função do append
    print(file3.read())


import os
os.remove('abc.text')  # apaga o arquivo criado.
