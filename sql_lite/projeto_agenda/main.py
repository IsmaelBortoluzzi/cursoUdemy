import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, ('%'+valor+'%',))  # busca por uma palavra ou num em algum lugar

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)

        for i in self.cursor.fetchall():
            print(i)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':

    agenda = AgendaDB('agenda.db')

    # agenda.editar('Mário', '1234467', 6)
    agenda.excluir(6)
    agenda.inserir('Joao Carlos', '1234462')
    agenda.listar()

