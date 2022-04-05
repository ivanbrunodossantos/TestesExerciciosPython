#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#se quiser importar a biblioteca toda usar o código:
#import math
#num = float(input('Digite um número'))
#print('seu número real é: {} e seu número inteiro é: {}'.format(num, math.trunc(num)))
from math import trunc
num = float(input('Digite um número'))
print('seu número real é: {} e seu número inteiro é: {}'.format(num, trunc(num)))


