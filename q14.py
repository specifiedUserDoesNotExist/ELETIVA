"""
Leia um número decimal (até 3 dígitos) e escreva o seu equivalente em numeração romana.
"""

romano = ["D","C","L","X","V","I"]
lista = [0,0,0,0,0,0]

numero = int(input("Digite um número de três algarismos: "))

while True:
	if numero >= 500:
		lista[0] += 1
		numero = numero - 500
	elif numero >= 100:
		lista[1] += 1
		numero = numero - 100
	elif numero >= 50:
		lista[2] += 1
		numero = numerp - 50
	elif numero >= 10:
		lista[3] += 1
		numero = numero - 10
	elif numero >= 5:
		lista[4] += 1
		numero = numero - 5
	elif numero >= 1:
		lista[5] += 1
		numero = numero - 1
	else:
		break

for i in range(6):
	if lista[i] == 4:
		print(romano[i]+romano[i-1], end="")
	else:
		print(romano[i]*lista[i], end="")

print()
