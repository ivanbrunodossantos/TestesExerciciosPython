#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento/
#de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
hoje = date.today().year
ano = int(input('Qual o ano de nascimento? : '))
idade = hoje - ano
if idade <= 9:
    print('você tem {} e é da categoria MIRIM'.format(idade))
elif 14 >= idade >= 9:
    print('Você tem {} e é da categoria INFANTIL'.format(idade))
elif 19 >= idade >= 14:
    print('Você tem {} e é da categoria JÚNIOR'.format(idade))
elif 25 >= idade >= 19:
    print('Você tem {} e é da categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('Você tem {} e é da categoria MASTER'.format(idade))









