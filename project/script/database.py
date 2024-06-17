import sqlite3
#Esta linha importa o módulo sqlite3 para o seu script Python. Este módulo fornece as 
# ferramentas necessárias para interagir com bancos de dados SQLite.

connection = sqlite3.connect('reconhecimento.db')
cursor = connection.cursor()
#Esta linha cria uma conexão com o banco de dados SQLite chamado "reconhecimento.db". 
# Se o banco de dados não existir, ele será criado automaticamente 
# neste local. A variável connection armazena essa conexão
#Esta linha cria um cursor a partir da conexão. O cursor é usado para
#  executar comandos SQL no banco de dados. A variável cursor 
# armazena esse cursor.