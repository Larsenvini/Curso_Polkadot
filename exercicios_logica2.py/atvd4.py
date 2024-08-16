palavra = input("Diga uma palavra/frase para ver se é um palindromo: ").replace(" ", "").lower()


if palavra[-1:0:-1] == palavra[0:-1:1]:
    print("Sua palavra/frase é um palindromo")
    
else:
    print("Sua palavra/frase não é um palindromo")