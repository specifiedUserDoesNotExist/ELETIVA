"""
Escreva um algoritmo que leia 2 valores (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x=y=0).
"""

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x > 0:
	if y > 0:
		print("(%.2f, %.2f) está no 1° quadrante" %(x,y))
	elif y < 0:
		print("(%.2f, %.2f) está no 4° quadrante" %(x,y))
	else:
		print("(%.2f, %.2f) está no sobre o eixo x" %(x,y))
elif x < 0:
	if y > 0:
		print("(%.2f, %.2f) está no 2° quadrante" %(x,y))
	elif y < 0:
		print("(%.2f, %.2f) está no 3° quadrante" %(x,y))
	else:
		print("(%.2f, %.2f) está no sobre o eixo x" %(x,y))
else:
	if y == 0:
		print("(%.2f, %.2f) está na origem" %(x,y))
	else:
		print("(%.2f, %.2f) está no sobre o eixo y" %(x,y))
