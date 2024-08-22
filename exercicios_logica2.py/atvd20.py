def calcular_media(lista):
    return sum(lista) / len(lista)

def main():
    numeros = []
    
    print("Digite números para adicionar à lista. Digite 'fim' para terminar.")
    
    while True:
        entrada = input("Digite um número: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Erro: Por favor, insira um número válido.")
    
    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        media = calcular_media(numeros)
        
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número foi inserido.")

if __name__ == "__main__":
    main()
