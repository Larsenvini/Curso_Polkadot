def soma_numeros():
    soma = 0  
    print("\nDigite números para somar. Digite 0 para encerrar.")
    
    while True:  
        try:
            numero = float(input("\nDigite um número: "))  

            if numero == 0:  
                break
            else:
                soma += numero  
        except ValueError:
            print("\nPor favor, insira um número válido.")
    
    print(f"\nA soma dos números digitados é: {soma}\n")

soma_numeros()
