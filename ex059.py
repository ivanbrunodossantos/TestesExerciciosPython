'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('digite o primeiro valor >>>'))
n2 = int(input('digite o segundo valor >>>'))
opção = 0
while opção != 5:
    print('''[1] somar
[2] multiplicar
[3] novos números
[4] maior
[5] sair do programa''')
    opção = int(input('digite a opção desejada >>> '))
    if opção == 1:
        soma = n1+n2
        print(f'o valor da soma é >>> {soma}')
    elif opção == 2:
        mult = n1*n2
        print(f'o valor da multiplicação é >>> {mult}')
    elif opção == 3:
        int(input('digite o primeiro número: '))
        int(input('digite o segundo número: '))
    elif opção == 4:
        if n1 < n2:
            print(f'o maior número é >>> {n2}')
        else:
            print(f'o maior número é >>> {n1}')

int(input('obrigado, volte sempre :-)'))























