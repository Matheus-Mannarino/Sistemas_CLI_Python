def adicionar_tarefa():
    id = int(input("Adicione uma ID para essa tarefa: "))
    nome = input("Insira o nome da tarefa: ")
    return {
        "ID": id,
        "Nome": nome
    }

def visualizar_tarefas(tarefas):
    busca = int(input("Insira a ID da tarefa que deseja visualizar: "))
    for tarefa in tarefas:
        if tarefa["ID"] == busca:
            print("Tarefa encontrada!\n")
            print(tarefa)
            return
    print("Tarefa não encontrada!")    

def atualizar_tarefas(tarefas):
    busca = int(input("Insira a ID da tarefa que deseja atualizar: "))
    for tarefa in tarefas:
        if tarefa["ID"] == busca:
            print(f"Tarefa encontrada: {tarefa['ID']} {tarefa['Nome']}\n")
            nova_id = input("Insira a ID da tarefa (deixe vazio para nao alterar): \n")
            novo_nome = input("Insira o novo nome da tarefa (deixe vazio para não alterar): \n")

            if nova_id.strip() != "":
                tarefa["ID"] = int(nova_id)
            elif novo_nome.strip() != "":
                tarefa["Nome"] = novo_nome
            print("Produto atualizado!")
            return
    print("Produto não encontrado!")                

def excluir_tarefas(tarefas):
    busca = int(input("Insira a ID da tarefa que deseja excluir: "))
    for tarefa in tarefas:
        if tarefa["ID"] == busca:
            print(f"Tarefa encontrada: {tarefa['ID']} {tarefa['Nome']}\n")
            tarefas.remove(tarefa)
            print("Tarefa excluida!")
            return
    print("Tarefa não encontrada!")


def menu():
    tarefas = []
    while True:
        print("\n--- Menu da Lista de Tarefas ---")
        print("1- Adicione uma nova tarefa")
        print("2- Visualizar tarefas adicionadas")
        print("3- Atualizar tarefas")
        print("4- Excluir tarefas")
        print("5- Sair")
        print("---------------------------------")
        menu = input("O que deseja fazer? ")

        if (menu == "1"):
            tarefas.append(adicionar_tarefa())

        elif (menu == "2"):
            visualizar_tarefas(tarefas)

        elif (menu == "3"):
            atualizar_tarefas(tarefas)

        elif (menu == "4"):
            excluir_tarefas(tarefas)

        elif (menu == "5"):
            break
        
        else:
            print("Opção inválida")

menu()        

        

            