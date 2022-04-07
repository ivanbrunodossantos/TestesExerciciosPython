#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Santos" no nome.

nome = str(input('qual o seu nome? ')).strip().upper().lower()
print('seu nome tem Santos? {}'.format('SANTOS'in nome.upper()))


