#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente:'))
hi = math.hypot(co, ca)
print('o valor da hipotenusa é: {:.2f}'.format(hi))


