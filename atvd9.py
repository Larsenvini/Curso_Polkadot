def ordenar_numeros(n1, n2, n3):
    numeros = [n1, n2, n3]
    
    numeros.sort()
    
    return numeros

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    numeros_ordenados = ordenar_numeros(num1, num2, num3)
    
    print("Os números em ordem crescente são:", numeros_ordenados)

if __name__ == "__main__":
    main()
