# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('qual o salário do funcionário?:'))
sr = s + (s*15/100)
print('o salário inicial do funcionário era :R${:.3f} e com aumento foi para: R${:.3f}'.format(s, sr))


