def calcular_soma_naturais(n):
    soma = n * (n + 1) // 2
    return soma

def main():
    try:
        n = int(input("Digite um número natural n: "))
        
        if n < 0:
            print("Por favor, insira um número natural positivo.")
        else:
            soma = calcular_soma_naturais(n)
            print(f"A soma dos primeiros {n} números naturais é: {soma}")
    
    except ValueError:
        print("Erro: Por favor, insira um número natural válido.")

if __name__ == "__main__":
    main()
