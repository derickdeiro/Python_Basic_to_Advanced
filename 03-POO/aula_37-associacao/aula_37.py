from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Joãozinho')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever()
print(maquina)

escritor.ferramenta = caneta  # associa a Class Escritor com a Caneta
escritor.ferramenta.escrever()
