def inverter_string(s):
    return s[::-1]

def main():
    string_usuario = input("Digite uma string: ")

    string_invertida = inverter_string(string_usuario)
    
    print(f"A string invertida é: {string_invertida}")

if __name__ == "__main__":
    main()
