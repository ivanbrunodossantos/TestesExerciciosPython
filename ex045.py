#Crie um programa que faça o computador jogar Jokenpô com voce
from time import sleep
from random import randint

lista = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções  
[0] pedra
[1] papel
[2] tesoura''')
voce = int(input('Escolha sua jogada: '))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)
print('o computador escolheu {} e você {} '.format(lista[computador], lista[voce]))
if computador == 0: #pedra
    if voce == 0:
        print('EMPATE')
    elif voce == 1:
        print('VOCE GANHOU')
    elif voce == 2:
        print('VOCÊ PERDEU')
    else:
        print('jogada inválida')
if computador == 1: #papel
    if voce == 0:
        print('VOCÊ PERDEU')
    elif voce == 1:
        print('EMPATE')
    elif voce == 2:
        print('VOCÊ GANHOU')
    else:
        print('jogada inválida')
if computador == 2: #tesoura
    if voce == 0:
        print('VOCÊ GANHOU')
    elif voce == 1:
        print('VOCÊ PERDEU')
    elif voce == 2:
        print('EMPATE')
    else:
        print('jogada inválida')







