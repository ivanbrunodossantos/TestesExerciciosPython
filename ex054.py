''' Crie um programa que leia o ano de nascimento de sete pessoas. No final,/
 mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano a {} nasceu?'.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('O total de pessoas maiores é de : {} '.format(totmaior))
print('o total de pessoas menores é de {} '.format(totmenor))

