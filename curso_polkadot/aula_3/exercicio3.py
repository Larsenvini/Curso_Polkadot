# programa que captura dados (nome e UF) sobre 3 estados do brasil, e os adiciona a lista brasil
def opca():
	
    n = input("Quer adicionar um estado? ")
    return n
     
def capturar_dados_estados():
    brasil = []

    for i in range(3):
        print(f"Estado {i+1}:")

        nome = input("Digite o nome do estado: ")

        uf = input("Digite a UF do estado: ")

        estado = {
            "nome": nome,
            "UF": uf
        }

        brasil.append(estado)

    return brasil

def main():
    
    s = opca()

    if s == "Sim":
        estados_brasil = capturar_dados_estados()
    
        print("\nDados dos estados:")
        for estado in estados_brasil:
            print(f"Estado: {estado['nome']}, UF: {estado['UF']}")
    else:
        opca()
if __name__ == "__main__":
    main()

