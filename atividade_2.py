def get_filme_e_ano():
    print("\nOlá!")
    while True:
        filme: str = input("\nQual seu filme favorito? ")
        if filme:
            filme = filme.capitalize()
            break
        print("Entrada inválida! Por favor, digite o nome de um filme.")

    
    while True:
        try:
            ano: int = int(input("\nEm que ano ele foi lançado? "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um ano válido em formato numérico.")
            break

    print(f"\nSeu filme favorito é {filme}!\n{filme} foi lançado em {ano}.\n")

get_filme_e_ano()
