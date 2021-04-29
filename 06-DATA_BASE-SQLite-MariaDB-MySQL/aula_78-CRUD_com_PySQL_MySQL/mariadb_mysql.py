import pymysql.cursors
from contextlib import contextmanager


# CRUD == CREAT, READ, UPDATE, DELETE

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password=None,
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


# INSERTE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()


# INSERE VARIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55)
#         ]
#
#         # executando diversas inserções no BD de uma vez
#         cursor.executemany(sql, dados)
#
#         conexao.commit()

# REMOVE UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (10,))
#         conexao.commit()

# REMOVE UM DETERMINADO NUMERO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# REMOVE REGISTROS DENTRO DE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (11, 13))
#         conexao.commit()


# ATUALIZA UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('JOANA', 5))
        conexao.commit()

# ESTE SELECIONA OS DADOS DA BD
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
