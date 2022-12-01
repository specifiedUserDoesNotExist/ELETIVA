"""
Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo usuário para Km/h. Para tal, multiplique o valor em m/s por 3,6
"""

v = float(input("Digite velocidade: "))

print("%.2f m/s é igual a %.2f km/h" %(v, 3.6*v))
