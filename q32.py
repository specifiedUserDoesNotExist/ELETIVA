"""
Escreva um programa que leia um caracter e diga se ele é uma vogal, consoante, número ou um símbolo (qualquer outro caracter, que não uma letra ou número).
"""

c = input("Digite um caracter: ")

if len(c) > 1:
	print("Error! Digite apenas um caracter.")
else:
	if 48 <= ord(c) <= 57:
		print("%s é um algarismo" %c)
	elif 65 <= ord(c) <= 90:
		if c in "AEIOU":
			print("%s é uma vogal maiúscula" %c)
		else:
			print("%s é uma consoante maiúscula" %c)
	elif 97 <= ord(c) <= 122:
		if c in "aeiou":
			print("%s é uma vogal minúscula" %c)
		else:
			print("%s é uma consoante minúscula" %c)
	else:
		print("%s é um símbolo" %c)
