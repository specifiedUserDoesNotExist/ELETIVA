"""
Escreva um programa para gerar o invertido de um número com três algarismos (exemplo: o invertido de 498 é 894).
"""

import math

num = int(input("Digite um número com três algarimos: "))

if math.log10(num) >= 3:
	print("Error! Digite número com três algarismo")
elif math.log10(num) < 2:
	print("Error! Digite número com três algarismo")
else:
	uni = num%10
	num_ = (num - uni)/10
	dez = num_%10
	cen = (num_ - dez)/10
	
	num_ = 100*uni+10*dez+cen
	print("O invertido de %d é %d" %(num, num_))
