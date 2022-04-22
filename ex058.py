'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. /
Só que agora o jogador vai tentar adivinhar até acertar, /
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep

print('-' * 23)
print('QUE OS JOGOS COMECEM!!!')
print('-' * 23)
pc = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jog = int(input('em que número eu estou pensando? '))
    palpite += 1
    if jog == pc:
        acertou = True
    else:
        if jog < pc:
            print('mais!!! tente mais uma vez')
        elif jog > pc:
            print('menos!!! tente mais uma vez')
print(f'Parabens você acertou com {palpite} palpites!!!')


