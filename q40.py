"""
Escreva um programa que receba um numero inteiro de 1 a 1000 e mostre na tela o numero por extenso.
"""

a = {
	0: "",
	1: "um",
	2: "dois",
	3: "três",
	4: "quatro",
	5: "cinco",
	6: "seis",
	7: "sete",
	8: "oito",
	9: "nove",
	10: "dez",
	11: "onze",
	12: "doze",
	13: "treze",
	14: "quartoze",
	15: "quinze",
	16: "dezesseis",
	17: "dezessete",
	18: "dezoito",
	19: "dezenove",
	20: "vinte",
	30: "trinta",
	40: "quarenta",
	50: "cinquenta",
	60: "sessenta",
	70: "setenta",
	80: "oitenta",
	90: "noventa",
	100: "cento",
	200: "duzentos",
	300: "trezentos",
	400: "quatrocentos",
	500: "quinhentos",
	600: "seiscentos",
	700: "setecentos",
	800: "oitocentos",
	900: "novecentos"
}

while True:
	texto = ""

	numero = int(input("Digite um número [0 (zero) para finalizar]: "))

	unidade = numero%10
	dezena = numero%100//10
	centena = numero%1000//100
	unidadeMilhar = numero//1000

	if numero > 1000:
		print("Error! Escolha um número inteiro de 1 a 1000!")
		continue
	elif numero == 0:
		print("Até a próxima!")
		break

	if dezena <= 1:
		texto = a[dezena*10+unidade]
	else:
		texto = a[dezena*10]+" e " + a[unidade]

	if unidadeMilhar == 1:
		if centena > 0:
			texto = "mil, " + a[centena*100]+ " e " + texto
		else:
			texto = "mil" + " e " + texto
	else:
		if centena > 0:
			texto = a[centena*100]+ " e " + texto

	if numero == 100:
		texto = "cem"
	if numero == 1000:
		texto = "mil"

	print(texto)	
