"""
Escreva um programa que calcule a raiz de uma equação do primeiro grau.
"""

a = float(input("Digite o termo 'a': "))
b = float(input("Digite o termo 'b': "))

if a == 0:
	print("Error! O termo 'a' deve ser diferente de zero!")
else:
	if b>0:
		print("A solução da equação %.2fx+%.2f=0 é %.2f" %(a, b, -b/a))
	elif b<0:
		print("A solução da equação %.2fx-%.2f=0 é %.2f" %(a, -b, -b/a))
	else:
		print("A solução da equação %.2fx=0 é %.2f" %(a, 0))
