"""
Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida. Em seguida, mostre-os em ordem crescente e decrescente.
"""


a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))

maior = 0
meio = 0
menor = 0


if a >= b >= c:
	maior = a
	meio = b
	menor = c
elif a >= c >= b:
	maior = a
	meio = c
	menor = b
elif b >= c >= a:
	maior = b
	meio = c
	menor = a
elif b >= a >= c:
	maior = b
	meio = a
	menor = c
elif c >= a >= b:
	maior = c
	meio = a
	menor = b
else:
	maior = c
	meio = b
	menor = a

print("Os números: %d %d %d" %(a,b,c))

print("Em ordem decrescente: %d %d %d" %(maior, meio, menor))

print("Em ordem crescente: %d %d %d" %(menor, meio, maior))
