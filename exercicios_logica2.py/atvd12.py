import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu escolhi um número entre 1 e 100.")
    
    while True:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("O palpite deve ser um número entre 1 e 100.")
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    jogar_adivinhacao()
