# programa pra calcular reducao de tempo de vida de um fumante
# um cigarro = 10 min perdidos
# dividir em perguntas

def main():
    
    Idade = int(input("Quantos anos você tem? ")) 
    cigarros_por_dia = int(input("Quantos cigarros fuma por dia? "))
    tempo = int(input("Fuma a quantos anos? "))
        
    perda_atual = ((10*cigarros_por_dia*365*tempo)//(60 * 24)) #total em dias perdidos
    
    print(f"Você já perdeu {round(perda_atual)} dias de sua vida por fumar, ou {perda_atual / 365} anos. Se você parar hoje, considerando a expectativa de vida média, viveria até {80-(int(perda_atual/365))} anos")

if __name__ == "__main__":
    main()