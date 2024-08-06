def traduzir(frase):
    nova_frase = ''
    
    for caractere in frase:
        
        if caractere in 'aeiouAEIOU':
            nova_frase += 'G'
        else:
            nova_frase += caractere
            
    return nova_frase

def pegar_frase():
    print("\n---------------------------------------\nBem vindo ao traduto maluco do Larsen!!\n---------------------------------------")
    frase = input("\nDigite uma frase: ")
    return frase

def main():
    opa = pegar_frase()
    frase_traduzida = traduzir(opa)
    print("\nFrase traduzida:", frase_traduzida, end ="\n\n")

if __name__ == "__main__":
    main()