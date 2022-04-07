#Faça um programa que leia o nome completo de uma pessoa/
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite um nome: ')).strip()
print('prazer em conhece-lo {}'.format(nome))
nome = nome.split()
print('seu primero nome é: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome)-1]))
