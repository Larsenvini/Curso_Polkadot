import math

def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

def main():
    try:
        raio = float(input("Digite o raio do círculo: "))
        
        if raio < 0:
            print("O raio não pode ser negativo. Tente novamente.")
        else:
            area = calcular_area_circulo(raio)
            print(f"A área do círculo com raio {raio} é {area:.2f}")
    except ValueError:
        print("Por favor, insira um número válido para o raio.")

if __name__ == "__main__":
    main()
