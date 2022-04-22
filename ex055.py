'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''


lista = []
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lista += [peso]
print('')
print('O Maior peso foi:', max(lista))  #maximo valor da lista
print('O Menor peso foi:', min(lista))  #minimo valor da lista
