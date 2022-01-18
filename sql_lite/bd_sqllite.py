import sqlite3

conexao = sqlite3.connect("basededados.db")
cursor = conexao.cursor()

"""
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
"""

"""
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Ismael Bortoluzzi", 56.1))

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': "Joao Pedro", 'peso': 56.1}
)

cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': "Daniel Almeida", 'peso': 96.1}
)
conexao.commit()
"""

"""
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Joana', 'id': 2}
)
"""

"""
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 8}
)
conexao.commit()
"""

cursor.execute('SELECT nome, peso FROM clientes WHERE peso < :peso', {'peso': 60})


# cursor.execute("SELECT * FROM clientes")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
