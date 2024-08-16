def calc_imc(w, h):
    grams = w * 1000
    imc = grams / (h*h)
    return imc

def format_imc(imc):
    imc_str = str(imc)[:4]
    
    imc_formatado = f"{imc_str[:2]},{imc_str[2:]}"
    
    return imc_formatado

def main():
    print("\nBem-vindo ao calculador de IMC!")
    altura = float(input("\nQual sua altura? (Use 1.??): "))
    peso = int(input("\nQual seu peso em kg? (Arredonde): "))
    
    imc = calc_imc(peso, altura)
    imc_formatado = format_imc(imc)
    
    print(f"\nSeu IMC é {imc_formatado}!")   
    
if __name__ == "__main__":
    main()