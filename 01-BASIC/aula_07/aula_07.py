nome = 'Derick'
idade = 29
altura = 1.73
e_maior = idade > 18
peso = 73.5
imc = peso/altura ** 2

print(nome, 'tem', idade, 'anos.', 'Seu IMC é:', imc,'É maior de 18 anos? [True/False]', e_maior)
print(f'{nome} tem {idade} anos. Seu IMC é: {imc:.2f}. É maior de 18 anos? [True/False] {e_maior}')
print('{} tem {} anos. Seu IMC é: {}. É maior de 18 anos? [True/False]{}' .format(nome, idade, imc, e_maior))
