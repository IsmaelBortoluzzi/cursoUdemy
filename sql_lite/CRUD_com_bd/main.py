import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


# with conectar() as conexao:
#     with conexao.cursor() as cursor1:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('Muriel', 'Figueiredo', '19', '60'),
#             ('Rosa', 'Padilha', '20', '60'),
#             ('Jose', 'Augusto', '30', '90'),
#         ]
#         cursor1.executemany(sql, dados)
#         conexao.commit()

with conectar() as conexao:
    with conexao.cursor() as cursor1:
        sql = 'DELETE FROM clientes WHERE id = %s'

        cursor1.execute(sql, (6,))
        conexao.commit()


with conectar() as conexao:
    with conexao.cursor() as cursor:

        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100 ')
        result = cursor.fetchall()

        for linhas in result:
            print(linhas)

        # cursor.close()
        # conexao.close()
