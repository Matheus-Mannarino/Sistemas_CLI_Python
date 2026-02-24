def cadastro_aluno():
            matricula = int(input("Insira a matrícula do aluno: "))
            nome = input("Insira o nome do aluno: ")
            notas = []
            for i in range(3):
                nota = float(input(f"Insira a {i + 1} nota: "))
                notas.append(nota)
            media = sum(notas) / len(notas)
            return {
                "Matricula": matricula, 
                "Nome": nome,
                "Notas": ", ".join(f"{nota:.2f}" for nota in notas),
                "Média": media
            }
      
def exibir_alunos(turma):
    if not turma:
        print("Nenhum aluno cadastrado")
    else:
        print("\n--- Alunos Cadastrados ---")
        for aluno in turma:
            print(f"Matrícula: {aluno['Matricula']}")
            print(f"Nome: {aluno['Nome']}")
            print(f"Notas: {aluno['Notas']}")
            print(f"Média: {aluno['Média']:.2f}")
            print("-------------------------------")

def salvar_dados(turma):
    with open("turma.txt", "w") as file:
        for aluno in turma:
            file.write(f"Matrícula: {aluno['Matricula']}\n") 
            file.write(f"Nome: {aluno['Nome']}\n") 
            file.write(f"Notas: {aluno['Notas']}\n") 
            file.write(f"Média: {aluno['Média']:.2f}\n") 
            file.write(f"-------------------------------\n")
        print("Dados Salvos")     
     
def principal():
    turma = []
    while True:
        print("1- Cadastro de Aluno")
        print("2- Exibir Alunos Cadastrado")
        print("3- Salvar Dados")
        print("4- Sair")
        menu = input("Digite sua opção: ")

        if(menu == "1"):
            turma.append(cadastro_aluno())

        elif(menu == "2"):
            exibir_alunos(turma)
        
        elif(menu == "3"):
            salvar_dados(turma)
        
        elif(menu == "4"):
            break
        
        else:
            print("Opção inválida")


principal()      