import sqlite3 as sql


conn = sql.connect('reconhecimento.db')
cursor = conn.cursor()

# Com o Unique, previne dados repetidos. Erro no `except` da `main.py`.

cursor.execute("""

CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT NULL ,
    cargo TEXT NULL ,
    email TEXT NULL ,	
    cpf VARCHAR(11) NULL ,
    identif VARCHAR(11) NULL

);

""")

print("A criação das tabelas com as colunas foi feita!")

conn.close()
