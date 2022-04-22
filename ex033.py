# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('digite o primeiro número'))
b = int(input('digite o segundo número'))
c = int(input('digite o terceiro número'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior foi {}'.format(maior))
print('O menor foi {}'.format(menor))
