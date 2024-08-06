# crie um dicionario e permita que o usuario possa atualizar um valor especifico de uma pessoa e adicionar pessoa

def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1. Mostrar pessoas")
    print("2. Adicionar uma pessoa")
    print("3. Atualizar informação de uma pessoa")
    print("4. Sair")

def mostrar_pessoas(pessoas):
    print("\nPessoas cadastradas:")
    for chave, info in pessoas.items():
        print(f"Nome: {chave}, Idade: {info['idade']}")

def atualizar_pessoa(pessoas):
    nome = input("\nDigite o nome da pessoa que deseja atualizar: ")

    if nome in pessoas:
        print("\nEscolha o que deseja atualizar:")
        print("1. Idade")

        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            nova_idade = int(input("Digite a nova idade: "))
            pessoas[nome]['idade'] = nova_idade
            print(f"\nIdade de {nome} atualizada para {nova_idade}.")
        else:
            print("\nOpção inválida!")
    else:
        print(f"\nPessoa com o nome '{nome}' não encontrada!")

def usuario_add(pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    pessoas[nome] = {"idade": idade}
    print(f"\nPessoa {nome} adicionada com sucesso!")

def main():
    pessoas = {
        "Alice": {"idade": 30},
        "Bruno": {"idade": 25},
        "Carla": {"idade": 28}
    }

    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção: ")
        
        if opcao == "1":
            mostrar_pessoas(pessoas)
        elif opcao == "2":
            usuario_add(pessoas)
        elif opcao == "3":
            atualizar_pessoa(pessoas)
        elif opcao == "4":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()


