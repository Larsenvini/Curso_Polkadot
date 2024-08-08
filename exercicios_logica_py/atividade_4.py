def pegar_temperatura():
    temperatura :int = int(input("\nQual a temperatura? "))

    if temperatura <= 15:
        print("\nBrrr, que frio.\n")
    
    elif temperatura >= 30:
        print("\nQuente demais! Puro suco do RJ PPRT!\n")
    
    elif temperatura >15 and temperatura <30:
        print("\nTemperatura ótima! :D\n")
        
pegar_temperatura()