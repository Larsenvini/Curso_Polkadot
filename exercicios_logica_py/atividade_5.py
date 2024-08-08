números = [0,1,2,3,4,5,6,7,8,9,10]

def printar_num():
    print(f"\nEsses são os números: {números}\n")
    
def pares():
    for i in números:
     if i %2==0:
         print(f"E esses são apenas os números pares: {i}")
    print("\n")
         
printar_num()
pares()