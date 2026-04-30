import sqlite3 as conector
conexao = conector.connect("estacioTeste.db")
cursor = conexao.cursor()

while True:
    print(" ----- MENU ------")
    print("""
    1 - Cadastrar Aluno
    2 - Listar Alunos
    3 - Sair 
""")
    op = input("Escolha a opção(1-3): ")
    
    if op == "1":
        nomeAluno = input("Digite o nome do aluno: ")
        cursoAluno = input("Digite o nome do curso: ")
        
        cursor.execute("INSERT INTO alunos (nome,curso) VALUES (?,?)", (nomeAluno, cursoAluno))## comando para inserir no banco de dados
        conexao.commit() ##envia para o banco de dados
        
        print("Adicionado!")
        
    elif op == "2":
        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall()
        for alunos in dados:
            print(alunos)
            
    elif op == "3":
        break

print("Voce saiu do menu!")