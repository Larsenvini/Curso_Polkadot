from utils import bem_vindo, pegar_letra, check, vencedor_ou_nao, exibir_bonequinho
from random import choice
from lista import palavras

def main():
    palavra = choice(palavras).lower()
    digitadas = []
    erros = 0
    max_erros = 6  

    bem_vindo()
    
    while erros < max_erros:
        letra = pegar_letra(digitadas)

        # tentativa repetida
        if letra in digitadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # adiciona letras certa
        digitadas.append(letra)

        # adiciona teentaiva errada
        if letra not in palavra:
            erros += 1
            exibir_bonequinho(erros)
        else:
            print("Boa escolha! A letra está na palavra.")

        #progresso da palavra
        secreto_temporário = check(digitadas, palavra)
        print(f"Palavra: {secreto_temporário}\n")

        #venceu
        if secreto_temporário == palavra:
            vencedor_ou_nao(palavra, True)
            break

    #esgota tentaivas
    if erros >= max_erros:
        vencedor_ou_nao(palavra, False)

if __name__ == '__main__':
    main()
