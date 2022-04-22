# Escreva um programa em Python que leia um número inteiro qualquer /
#e peça para o usuário escolher qual será a base de conversão: /
#1 para binário, 2 para octal e 3 para hexadecimal.

nun = int(input('Digite um número: '))
print('''escolha uma das bases para conversão
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opc = int(input('escolha uma das opções: '))
if opc == 1:
    print('o numero {} convertido para binário é igual a {}'.format(nun, bin(nun)[:2]))
elif opc == 2:
    print('o numero {} convertido para octal é igual a {}'.format(nun, oct(nun)[:2]))
elif opc == 3:
    print('o numero {} convertido para hexadecimal é igual a {}'.format(nun, hex(nun)[:2]))
else:
    print('opção inválida')






