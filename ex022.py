#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao não considerando os espaços
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
print('analisando seu nome ele tem...')
print('seu nome em letras maiúsculas é: {}.'.format(nome.upper()))
print('seu nome em letras minusculas é: {}.'.format(nome.lower()))
print('seu nome tem ao todo tem: {} letras.'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem: {} letras.'.format(nome.find(' ')))





