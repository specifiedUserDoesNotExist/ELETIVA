"""
Escreva um programa que leia um valor e imprima todas as possíveis combinações em que o lançamento de um par de dados tenha como resultado da soma dos valores dos dados o número lido.
"""

n = int(input("Digite um número entre 2 e 14: "))


if 2 <= n <= 14:
	print("As possíveis combinações são: ", end="")
	for i in range(1,7):
		for j in range(i,7):
			if i+j == n:
				print("%d e %d" %(i,j), end=", ")
	print(".")
else:
	print("Error! Tente novamente!")

print()
