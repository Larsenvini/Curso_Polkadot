def somar_pares():
    soma = 0
    # iterando de 1 até 100
    for numero in range(1, 101):
        # verificando se o número é par
        if numero % 2 == 0:
            soma += numero  # adicionando à soma acumulada
    
    return soma

def main():
    # chamando a função e exibindo o resultado
    soma_total = somar_pares()
    print(f"A soma de todos os números pares entre 1 e 100 é: {soma_total}")

if __name__ == "__main__":
    main()

