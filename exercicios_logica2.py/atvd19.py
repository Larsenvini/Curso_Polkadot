def calcular_media_ponderada(nota1, nota2, nota3, peso1=2, peso2=3, peso3=5):
    # calculando a média ponderada
    soma_ponderada = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    soma_pesos = peso1 + peso2 + peso3
    media_ponderada = soma_ponderada / soma_pesos
    return media_ponderada

def main():
    try:
        # solicitando ao usuário que insira as três notas
        nota1 = float(input("Digite a primeira nota (peso 2): "))
        nota2 = float(input("Digite a segunda nota (peso 3): "))
        nota3 = float(input("Digite a terceira nota (peso 5): "))
        
        # chamando a função para calcular a média ponderada
        media = calcular_media_ponderada(nota1, nota2, nota3)
        
        # exibindo o resultado
        print(f"A média ponderada das notas é: {media:.2f}")
    
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para as notas.")

if __name__ == "__main__":
    main()
