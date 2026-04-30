import sqlite3 as conector
## abre uma conexão com o banco de dados

conexao = conector.connect("estacioTeste.db")
cursor = conexao.cursor()


# nomeAluno = input("Digite o nome do aluno: ")
# cursoAluno = input("Digite o curso matriculado: ")

# cursor.execute("INSERT INTO alunos (nome, curso) VALUES (?,?)", (nomeAluno, cursoAluno))

# cursor.execute("DELETE FROM alunos WHERE id_aluno=3 ")c

# cursor.execute(""" SELECT * FROM alunos """)
# dados = cursor.fetchall()

# for aluno in dados:
#     print(aluno)



conexao.commit()