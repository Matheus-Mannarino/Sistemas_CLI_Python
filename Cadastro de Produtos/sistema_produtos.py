def criar_produto():
    id = int(input("Insira a ID do produto: "))
    produto = input("Insira o nome do produto: ")
    preco = float(input("Insira o preço do produto: "))
    quantidade = int(input("Insira a quantidade de produtos existentes: "))
    return {
        "ID": id,
        "Produto": produto,
        "Preço": preco,
        "Quantidade": quantidade
    }

def exibir_produto(produtos):
    busca = int(input("Insira a ID do produto que deseja buscar: "))
    for produto in produtos:
        if produto["ID"] == busca:
            print("Produto Encontrado:\n")
            print(f"{produto}\n")
            return
    print("Produto não encontrado") 

def atualizar_produto(produtos):
    busca = int(input("Insira a ID do produto que deseja atualizar: "))
    for produto in produtos:
        if produto["ID"] == busca:
            print(f"Produto encontrado: {produto['Produto']} (Preço: {produto['Preço']}, Quantidade: {produto['Quantidade']})")
            novo_preco = input("Insira o novo preço do produto (deixe vazio para nao alterar): ")
            nova_quantidade = input("Insira a nova quantidade de produtos (deixe vazio para não alterar): ")

            if novo_preco.strip() != "": #se o novo preço após remover os espaços(strip) for diferente de vazio, vai atualizar
                produto["Preço"] = float(novo_preco)
            elif nova_quantidade.strip() != "": #se a nova quantidade após remover os espaços for diferente de vazio, vai atualizar
                produto["Quantidade"] = int(nova_quantidade)
            print("Produto Atualizado!")
            return
    print("Produto não encontrado")

def excluir_produto(produtos):
    busca = int(input("Insira a ID do produto que deseja excluir: "))
    for produto in produtos:
        if produto["ID"] == busca:
            produtos.remove(produto)
            print("Produto excluído!")
            return
    print("Produto não encontrado")    

def menu():
    produtos = [
    {"ID": 101, "Produto": "Caneta", "Preço": 2.50, "Quantidade": 100},
    {"ID": 102, "Produto": "Caderno", "Preço": 15.00, "Quantidade": 50},
    {"ID": 103, "Produto": "Mochila", "Preço": 120.00, "Quantidade": 20},
    {"ID": 104, "Produto": "Estojo", "Preço": 8.00, "Quantidade": 30},
    {"ID": 105, "Produto": "Lápis", "Preço": 1.00, "Quantidade": 200}
    ]
    while True:
        print("1- Adicione um novo produto à lista")
        print("2- Exibir Produtos")
        print("3- Atualizar Produtos")
        print("4- Excluir Produtos")
        print("5- Sair")
        menu = input("Digite sua opção: ")

        if (menu == "1"):
            produtos.append(criar_produto())

        elif (menu == "2"):
            exibir_produto(produtos)

        elif (menu == "3"):
            atualizar_produto(produtos) 

        elif (menu == "4"):
            excluir_produto(produtos)       
    
        elif (menu == "5"):
            break
        
        else:
            print("Opção inválida")

menu()            