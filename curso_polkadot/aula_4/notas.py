def pegar_notas():
    notas = []
    print("\nInsira suas duas notas para saber seu status!")
    for i in range(2):
        try:
            nota = float(input("\nInsira sua nota: "))
            if nota < 0 or nota > 10:
                raise ValueError("\nNota deve estar entre 0 e 10.")
            notas.append(nota)
        except ValueError as e:
            print(e)
            return None
    
    media = sum(notas) / len(notas)
    return media
    
def aprovar(media):
    if media is None:
        print("\nNão foi possível calcular a média.")
        return
    
    if media < 7:
        print("\nReprovado")
    else:
        print("\nAprovado!\n")
        
def main():
    media = pegar_notas()
    aprovar(media)
    
if __name__ == "__main__":
    main()
