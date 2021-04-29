string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
# resolução Miranda - list Comprehension
lista1 = [string[i:i+n] for i in range(0, len(string), n)]  # conta de 0 até o tamanho da String indo de 10 em 10
print(lista1)
retorno1 = '.'.join(lista1)
print(retorno1)
