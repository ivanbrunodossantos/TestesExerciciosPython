#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

a = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format (a, c, c*a))


