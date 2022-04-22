#Faça um programa que leia o ano de nascimento de um jovem e informe, /
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, /
#se é a hora exata de se alistar ou se já passou do tempo do alistamento./
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('qual seu ano de nascimento?: '))
idade = atual - ano
print('quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('voce deve alistar-se no serviço militar neste ano de {}'.format(atual))
elif idade < 18:
    saldo1 = 18 - idade
    print('ainda falta {} anos para alistar-se'.format(saldo1))
elif idade > 18:
    saldo2 = idade - 18
    print('você ja passou {} anos do prazo para alistamento'.format(saldo2))





