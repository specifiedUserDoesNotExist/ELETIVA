"""
Escreva um programa que leia três números e mostre o maior entre eles.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

maior = n1

if n2 > maior:
	maior = n2

if n3 > maior:
	maior = n3
	
print("O maior dos números %d, %d, %d é %d" %(n1, n2, n3, maior))
