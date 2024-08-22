def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def main():
    frase = input("Digite uma frase: ")
    
    numero_palavras = contar_palavras(frase)
    
    print(f"A frase contém {numero_palavras} palavras.")

if __name__ == "__main__":
    main()
