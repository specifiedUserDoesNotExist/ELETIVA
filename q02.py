"""
Dado o tamanho do lado de um quadrado, calcular a área e o perímetro do mesmo.
"""

lado = float(input("Digite lado: "))

area = lado*lado
perimetro = 4*lado

print("Área = %.2f" %area)
print("Perímetro = %.2f" %perimetro)
