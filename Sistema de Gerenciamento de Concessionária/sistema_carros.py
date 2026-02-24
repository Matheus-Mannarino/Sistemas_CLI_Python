def cadastro_veiculo():
    veiculo = input("Insira seu veículo: ")
    tipo_veiculo = input("Insira o tipo do seu veículo: ")
    preco = float(input("Insira o preço do seu veículo: "))
    ano_fabricacao = int(input("Insira o ano de fabricação do seu veículo: "))
    return {
        "Veículo": veiculo,
        "Tipo do veículo": tipo_veiculo,
        "Preço": preco,
        "Ano de fabricação": ano_fabricacao
    }

def exibir(carros):
    if len (carros) == 0:
        print("Nenhum veículo cadastrado")
    else:
        for item in carros:
            print(f"\n--- Veículos Cadastrados ---") 
            print(f"Veículo: {item['Veículo']}")    
            print(f"Tipo do Veículo: {item['Tipo do veículo']}")    
            print(f"Preço: {item['Preço']}")    
            print(f"Ano de Fabricação: {item['Ano de fabricação']}")    
            print(f"-----------------------------------------------")

def buscar(carros):
    if len (carros) == 0:
        print("Nenhum veículo cadastrado")
    else:
        busca = input(f"Insira o Veículo que deseja buscar: ")
        for item in carros:
            if busca == item['Veículo']:
                print(f"Veículo: {item['Veículo']}")    
                print(f"Tipo do Veículo: {item['Tipo do veículo']}")    
                print(f"Preço: {item['Preço']}")    
                print(f"Ano de Fabricação: {item['Ano de fabricação']}")    
                print(f"-----------------------------------------------")
            else:
                print("Veículo não encontrado")    

def salvar(carros):
    with open ('veiculos.txt', "w") as file:
        for item in carros:
            file.write(f"Veículo: {item['Veículo']}\n")
            file.write(f"Tipo de Veículo: {item['Tipo do veículo']}\n")
            file.write(f"Preço: {item['Preço']}\n")
            file.write(f"Ano de Fabricação: {item['Ano de fabricação']}\n")
            file.write(f"------------------------------------------------")
        print("Dados Salvos")    


def home():
    carros = []
    while True:
        print("1- Cadastro de Veículo")
        print("2- Exibir os Veículos Cadastrados")
        print("3- Buscar Veículos")
        print("4- Salvar Dados")
        print("5- Sair")
        menu = input("Insira sua opção: ")

        if (menu == "1"):
            carros.append(cadastro_veiculo())

        elif (menu == "2"):
            exibir(carros)

        elif (menu == "3"):
            buscar(carros)

        elif (menu == "4"):
            salvar(carros) 

        elif (menu == "5"):
            break

        else:
            print("Opção Inválida")

home()            

