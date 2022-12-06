"""
Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida. Em seguida, mostre-os em ordem crescente e decrescente.
"""


a = int(input("digite o primeiro numero"))
b = int(input("digite o segundo numero"))
c = int(input("digite o terceiro numero"))

maior = 0;
meio = 0;
menor = 0;


if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
    

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
    
if a != menor and b != maior:
    meio = c
elif a != menor and c != maior:
    meio = b
else:
    meio = a
    
    
print(a,b,c)
    
print(maior, meio, menor)

print(menor, meio, maior)
