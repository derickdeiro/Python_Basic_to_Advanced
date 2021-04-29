import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)  # valor inicial, valor final-1 pulando de X em X

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2)  # não repete os valores.
# sorteio = random.choices(lista, k=2)
# sorteio = random.choice(lista)

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters  # retorna letras maiúsculas e minúsculas
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))  # gera uma senha de 20 caracteres.

# print(senha)

for i in range(10):
    senha = "".join(random.choices(geral, k=20))
    print(senha)
    print()