def contar_vogais(frase):
    vogais = "aeiouAEIOU"  
    contador = 0  
    for letra in frase:
        
        if letra in vogais:
            contador += 1  

    return contador

def main():
    frase = input("Digite uma frase: ")
    
    numero_vogais = contar_vogais(frase)
  
    print(f"A frase contém {numero_vogais} vogais.")

if __name__ == "__main__":
    main()
