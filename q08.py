"""
Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), leu um valor de temperatura em Fahrenheit e exibi-lo em Celsius 
"""

f = float(input("Digite temperatura: "))

c = 5*(f-32)/9

print("%.2f°F = %.2f°C" %(f, c))
