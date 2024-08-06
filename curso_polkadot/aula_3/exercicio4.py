import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    print("\n\nBem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("\nUsaremos a regra melhor de 3 .")
    
    pontuacao_usuario = 0
    pontuacao_computador = 0
    rodadas = 1

    while rodadas <= 3:
        print(f"\nRodada {rodadas}:")
        
        
        escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

        if escolha_usuario not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue
        
    
        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu: {escolha_computador}")

    
        if escolha_usuario == escolha_computador:
            print("Empate nesta rodada!")
        elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
             (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
             (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
            print("\nVocê venceu esta rodada!")
            pontuacao_usuario += 1
        else:
            print("\nVocê perdeu esta rodada!")
            pontuacao_computador += 1
        
        
        rodadas += 1

    print("\nPontuação Final:")
    print(f"\nVocê: {pontuacao_usuario}")
    print(f"\nComputador: {pontuacao_computador}")


    if pontuacao_usuario > pontuacao_computador:
        print("Parabéns, você é o vencedor geral!")
    elif pontuacao_usuario < pontuacao_computador:
        print("O computador é o vencedor geral, que decepção!!")
    else:
        print("O jogo terminou em empate geral!")

jogar()
