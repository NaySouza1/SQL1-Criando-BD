# Utilizei o pip install mysql-connector-python
# Faça um script SQL que crie um banco de dados no MySql chamado: Infinity_School, salve este script e então execute-o.

import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario", #para proteção de dados troquei meu usuario por seu_usuario
    password="sua_senha" #idem sua_senha
)


cursor = conexao.cursor()


comando_sql = "CREATE DATABASE IF NOT EXISTS Infinity_School;"


cursor.execute(comando_sql)

print("Banco de dados 'Infinity_School' criado com sucesso.")


cursor.close()
conexao.close()
