def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def main():
    print("Calculadora Simples")
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        print("Escolha a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        operacao = input("Digite o símbolo da operação desejada (+, -, *, /): ")
        
        if operacao == '+':
            resultado = somar(numero1, numero2)
        elif operacao == '-':
            resultado = subtrair(numero1, numero2)
        elif operacao == '*':
            resultado = multiplicar(numero1, numero2)
        elif operacao == '/':
            resultado = dividir(numero1, numero2)
        else:
            resultado = "Operação inválida."

        print(f"Resultado: {resultado}")
    
    except ValueError:
        print("Erro: Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
