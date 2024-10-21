import sqlite3

def get_db_connection():
    conn = sqlite3.connect('identifier.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
conn.execute("""
    INSERT INTO funcionario (nome_funcionario,datanasc_funcionario,senha_funcionario,telefone_funcionario)
    VALUES (?, ?, ?, ?) """,("ramom", 22/33/2330, 123 , 40028922))

conn.commit()
conn.close()
