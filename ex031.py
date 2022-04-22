#Desenvolva um programa que pergunte a distância de uma viagem em Km. /
#Calcule o preço da passagem, cobrando R$0,50 por Km/
#para viagens de até 200Km e R$0,45 para viagens mais longas.
dis = float(input('Qual a distância da viagem? : '))
res1 = (dis * 0.50)
res2 = (dis * 0.45)
if dis  <= 200:
    print('voce irá pagar R$ {:.2f} na passagem'.format(res1))
else:
    print('você irá paagar R$ {:.2f} na passagem'.format(res2))







