'''
if, elif, else, and, not, or, in, out
'''

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'derick'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')
