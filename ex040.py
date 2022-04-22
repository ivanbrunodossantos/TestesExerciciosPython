# Crie um programa que leia duas notas de um aluno e calcule sua média, /
#mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('sua média foi de {} e está reprovado'.format(med))
elif 7 > med >= 5:
    print('Sua média foi de {} e está de recuperação'.format(med))
else:
    print('você foi aprovado!')








