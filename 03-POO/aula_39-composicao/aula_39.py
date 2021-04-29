from classes import Cliente  # não precisa importar o endereço pq na Class Cliente já está fazendo isso.

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1  # ao apagar o cliente, a COMPOSIÇÃO entre as Cliente e Endereco já realiza as duas operações.
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
print('#########################')
