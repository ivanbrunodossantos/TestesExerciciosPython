#Escreva um programa que leia a velocidade de um carro. /
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado./
#A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade atual do carro? :'))
if vel > 100:
    print('MULTADO!!! você está acima do limite permitido de velocidade que é de 80km/h')
    multa = (vel-100)*7
    print('você irá pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')

