import sqlite3

conexao = sqlite3.connect('basededados.db')  # por convenção, sempre utilziar .db
cursor = conexao.cursor()  # quem vai executar as funções dentro do DB

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# inserindo valores nos campos da tabela criada
# NÃO É SEGURO FAZER DA FORMA BAIXO, SQL Injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES("Derick Deiró", 77.6)')
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES(?, ?)', ("Maria", 50))  # Evita SQL Injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES(:nome, :peso)',
#     {'nome':'Joãozinho', 'peso': 25})
#
# cursor.execute(
#     'INSERT INTO clientes VALUES(:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 113})
#
# conexao.commit()  # executando o comando acima

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=id',
               {'nome': 'Joana', 'id': 2})
conexao.commit()
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=id',
               {'nome': 'Derick Deiró', 'id': 1})
conexao.commit()
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=id',
               {'nome': 'Joãozinho', 'id': 3})
conexao.commit()
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=id',
               {'nome': 'Daniel', 'id': 4})
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():  # busca os valores na tabela
    identificador, nome, peso = linha
    print(identificador, nome, peso)


# é importante sempre fechar a conexão e o cursor
cursor.close()
conexao.close()
