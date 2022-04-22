#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 /
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. /
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
pc = randint(0, 5)
print('-'*23)
print('QUE OS JOGOS COMECEM!!!')
print('-'*23)
jog = int(input('em que número eu estou pensando?'))
print('processando...')
sleep(2)
if jog == pc:
    print('Parabens você acertou :-( !!!')
else:
    print('eu ganhei kkkk!!! pensei no número {} e não no {}'.format(pc, jog))






