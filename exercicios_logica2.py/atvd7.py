def calcular_media():
    total_notas = 0
    contador = 0

    while True:
        nota = float(input("Digite uma nota (ou -1 para sair): "))
        if nota == -1:
            break
        total_notas += nota
        contador += 1

    if contador == 0:
        print("Nenhuma nota foi inserida.")
    else:
        media = total_notas / contador
        print(f"A média das notas é: {media:.2f}")

calcular_media()
