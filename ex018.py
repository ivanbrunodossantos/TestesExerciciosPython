#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o ângulo que deseja: '))
s = math.sin(math.radians(a))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, s))
c = math.cos(math.radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, c))
t = math.tan(math.radians(a))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, t))




