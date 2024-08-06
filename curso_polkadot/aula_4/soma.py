def soma_dois_numeros(numero1, numero2):
    if not (isinstance(numero1, (int, float)) and isinstance(numero2, (int, float))):
        raise ValueError("Só dá pra somar números, amigão.")
    
    resultado = numero1 + numero2
    return resultado

def main():
    try:
        num = input("Diga dois números pra somar, use x,y!\nOnde x é um número e y é outro: ")

        x_str, y_str = num.split(",")
        
        x = float(x_str)
        y = float(y_str)
   
        print(soma_dois_numeros(x, y))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
