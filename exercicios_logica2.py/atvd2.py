def converter_fahrenheit(degrees):
    fahrenheit = degrees * 9/5 +32
    return fahrenheit


def converter_kelvin(degrees):
    kelvin = degrees + 273.15
    return kelvin 
    
def main():
    print("\nBem vindo ao convertor de Celsius para Fahrenheit e Kelvin! \n\n Escolha uma opção:\n1. Converter para Fahrenheit\n2. Converter para Kelvin")
    opcao = int(input("\nPara qual unidade você quer converter? "))
    celsius = int(input("\nQual a temperatura em C? "))
    
    if opcao == 1:
        n = converter_fahrenheit(celsius)
        print(f"\n{n} Fahrenheits")
        
    elif opcao == 2:
        x = converter_kelvin(celsius)
        print(f"\n{x} Kelvin")
        
    else:
        print("\nOpcao nao existe, tente de novo")
        main()
        
if __name__ == "__main__":
    main()