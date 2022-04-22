# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. /
# Para salários superiores a R$1250,00, calcule um aumento de 10%. /
# Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o salário do funcionário? '))
sal10 = sal+(sal/100*10)
sal15 = sal+(sal/100*10)
if sal > 1250:
    print('seu salário que era de R$ {:.2f} terá um aumento de 10% e passará a ser de: R$ {:.2f}'.format(sal, sal10))
else:
    print('seu salário que era de R$ {:.2f} terá um aumento de 15% e passará a ser de: R$ {:.2f}'.format(sal, sal15))
print('tenha um ótimo dia!!!')




