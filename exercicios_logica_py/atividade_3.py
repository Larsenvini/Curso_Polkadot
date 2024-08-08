def main():
    print("\nCalculadora Básica")
    
    try:
        num1 = float(input("\nDigite o primeiro número: "))
    except ValueError:
        print("\nErr! Por favor, digite um número válido.")
        return
    
    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("\nErro! Por favor, digite um número válido.")
        return

    soma = num1 + num2
    print(f"\nSoma: {num1} + {num2} = {soma}")
    
    subtracao = num1 - num2
    print(f"\nSubtração: {num1} - {num2} = {subtracao}")
    
 
    multiplicacao = num1 * num2
    print(f"\nMultiplicação: {num1} * {num2} = {multiplicacao}")

  
    try:
        divisao = num1 / num2
        print(f"\nDivisão: {num1} / {num2} = {divisao}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

if __name__ == "__main__":
    main()
