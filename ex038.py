# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

nun1 = int(input('digite o primeiro número: '))
nun2 = int(input('digite o segundo número: '))
if nun1 > nun2:
    print('o primeiro valor é maior')
elif nun2 > nun1:
    print('o segundo valor é maior')
elif nun1 == nun2:
    print('Não existe valor maior, os dois são iguais')
print('tenha um bom dia')
#ou
#else:
#    print('Não existe valor maior, os dois são iguais')
#print('tenha um bom dia')