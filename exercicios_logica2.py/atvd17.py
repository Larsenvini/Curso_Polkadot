def eh_numero_perfeito(n):
    soma_divisores = 0

    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    
    return soma_divisores == n

def main():
    try:
        numero = int(input("Digite um número: "))
        
        if numero <= 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            if eh_numero_perfeito(numero):
                print(f"{numero} é um número perfeito.")
            else:
                print(f"{numero} não é um número perfeito.")
    
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
