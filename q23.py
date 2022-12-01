"""
Escreva um programa que leia um número e imprima se este número é ou não par.
"""

n = int(input("Digite um número: "))

if n%2 == 0:
	print("%d é par." %n)
else:
	print("%d é ímpar." %n)
