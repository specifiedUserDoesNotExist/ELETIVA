"""
Escreva um programa que calcule a raiz de uma equação do segundo grau.
"""
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

sgnB = ["+","-"][b/abs(b)<0]
sgnC = ["+","-"][c/abs(c)<0]

if a == 0:
	print("Error! 'a' deve ser um valor diferente de zero!")
else:
	delta = b*b-4*a*c
	
	if delta > 0:
		x1 = (-b+delta**(.5))/(2*a)
		x2 = (-b-delta**(.5))/(2*a)
		print("A equação %.2fx²%c%.2fx%c%.2f=0 possui duas raízes reais." %(a, sgnB, abs(b), sgnC, abs(c)))
		print("x1 = %.2f" %x1)
		print("x2 = %.2f" %x2)
	elif delta == 0:
		print("A equação %.2fx²%c%.2fx%c%.2f=0 possui apenas uma raiz real" %(a, sgnB, abs(b), sgnC, abs(c)))
		print("x = %.2f" %(-b/(2*a)))
	else:
		print("A equação %.2fx²%c%.2fx%c%.2f=0 não possiu raízes reais" %(a, sgnB, abs(b), sgnC, abs(c)))
