# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. /
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. /
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

sal = float(input('Qual o seu salário?'))
casa = float(input('Qaul o valor da casa?'))
ano = float(input('em quatos anos a casa será paga?'))
prest = casa /  (ano*12)
min = sal*30/100
print('para pagar uma casa de {:.2f} em {:.2f} anos'.format(casa,ano))
print('a prestação será de {:.2f} '.format(prest))
if prest <= min:
    print('emprestimo concedido')
else:
    print('emprestimo negado')

