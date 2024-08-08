
def lista_de_compras():
    compras = []  
    print("\nBem-vindo à sua lista de compras!")
    print("Digite 'sair' para finalizar e ver sua lista completa.\n")

    while True:
        item = input("Adicione um item à lista (Digite 'sair' para finalizar): ").strip()

        if item.lower() == 'sair':
            break

        if item:  
            compras.append(item)  
            print(f"'{item}' adicionado à lista.\n")
        else:
            print("Por favor, insira um item válido.\n")

    
    print("\nSua lista de compras completa é:")
    for i, item in enumerate(compras, start=1):
        print(f"{i}. {item}")
        print("\n")


lista_de_compras()
