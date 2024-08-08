def eh_primo(numero):
    """
    função para verificar se um número é primo

    
    tem como parametro = numero (int): o número a ser verificado

    retornmna um bool: True se o número for primo, False caso contrário
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(intervalo_inicio, intervalo_fim):
    """
    função para encontrar todos os números primos no intervalo dado

    parâmetros:
    intervalo_inicio (int): o início do intervalo (inclusivo)
    intervalo_fim (int): o fim do intervalo (inclusivo)
 
    retorna list: uma lista de números primos no intervalo especificado
    """
    primos = []
    for numero in range(intervalo_inicio, intervalo_fim + 1):
        if eh_primo(numero):
            primos.append(numero)
    return primos

def main():
    print("\nBem-vindo ao programa de busca de números primos em um intervalo!\n")
    
    try:
        intervalo_inicio = int(input("\nDigite o número inicial do intervalo: "))
        intervalo_fim = int(input("\nDigite o número final do intervalo: "))
    except ValueError:
        print("Por favor, insira números válidos!")
        return

    if intervalo_inicio > intervalo_fim:
        print("\nO número inicial deve ser menor ou igual ao número final!")
        return

    primos = encontrar_primos(intervalo_inicio, intervalo_fim)
    
    print(f"\nOs números primos no intervalo de {intervalo_inicio} a {intervalo_fim} são:\n")
    print(", ".join(map(str, primos)) if primos else "Nenhum número primo encontrado!")

if __name__ == "__main__":
    main()
