"""
Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro.
"""
b = float(input("Digite base: "))
h = float(input("Digite altura: "))

area = b*h
perimetro = 2*b+2*h

print("Área = %.2f" %area)
print("Perímetro = %.2f" %perimetro)
