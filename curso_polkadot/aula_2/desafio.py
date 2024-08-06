

from random import randint

a = 0
b = 0

while a or b < 30:
	print(f"Carro A: {a}, Carro B: {b}")
	a += randint(1,5)
	b += randint(1,5)
	if a > 30:
		print("Carro A é o vencedor")
		break
	elif b > 30:
		print("Carro B é o vencedor")
		break
