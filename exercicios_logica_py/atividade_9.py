def count():
    
    frase = input("\nDigite uma frase: ")
    
    letra = input("\nDigite uma letra pra contar: ")
   
    vezes = frase.lower().count(letra)
    
   
    if vezes <= 1:
        print(f"\nA letra {letra}, apareceu {vezes} vez na frase {frase}")
    else:
        print(f"\nA letra {letra}, apareceu {vezes} vezes na frase '{frase}'")
    
    print("\n")
    
count()    