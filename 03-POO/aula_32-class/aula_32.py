from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p1.comer('maçã')
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('banana')
p1.parar_comer()

p1.falar('POO')
p1.falar('Games')
p1.parar_falar()
p1.comer('laranja')

print('~' * 30)
print(p1.get_ano_nascimento())

