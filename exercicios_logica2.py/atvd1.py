def calc_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
'''Pense que a função é chamada com numero = 5.
Inicializamos fatorial = 1.
O loop começa com i = 1:
fatorial = 1 * 1 → fatorial = 1
Próxima iteração com i = 2:
fatorial = 1 * 2 → fatorial = 2
Próxima iteração com i = 3:
fatorial = 2 * 3 → fatorial = 6
Próxima iteração com i = 4:
fatorial = 6 * 4 → fatorial = 24
Próxima iteração com i = 5:
fatorial = 24 * 5 → fatorial = 120
'''
    
def main():
    print("\nBem vindo a calculadora de fatorial")
    _numero = int(input("\nDigite um número: "))
    
    _fatorial = calc_fatorial(_numero)
    
    print(f"\nO fatorial de {_numero} é {_fatorial} !")
    
if __name__ == "__main__":
    main()