def exibir_bonequinho(erros):
    bonequinho = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =====
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =====
        """
    ]
    print(bonequinho[erros])

def bem_vindo():
    print('-='* 20)
    print('         Jogo Da Força Python')
    print('-='* 20)

def pegar_letra(digitadas):
    while True:
        letra = str(input("Digite uma letra: ")).lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Digite apenas uma letra.')
        else:
            return letra

def check(digitadas, palavra):
    secreto_temporário = ""  
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreto_temporário += letra_secreta
        else:
            secreto_temporário += '*'
    return secreto_temporário  # Retorna o estado atual da palavra secreta

def vencedor_ou_nao(palavra, venceu):
    if venceu:
        print("Parabéns, você escapou e venceu!")
    else:
        print(f"Game Over! A palavra era: {palavra}.")
