'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. /
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho/
e quantas mulheres têm menos de 20 anos.'''

media = 0
mulhernova = 0
nomevelho = 0
idadevelho = 0
contahomem = 0

for pessoa in range(1, 5):
    print(f'---- {pessoa}ª pessoa ----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    media += idade
    if sexo == 'F':
        if idade < 20:
            mulhernova += 1

    if sexo == 'M':
        contahomem += 1
        if idade > idadevelho:
            idadevelho = idade
            nomevelho = nome

print(f'A média de idade do grupo é de {media/4:.2f} anos')
if mulhernova == 0:
    pass
else:
    print(f'Ao todo são {mulhernova} mulher(es) com menos de 20 anos.')
if contahomem == 0:
    pass
else:
     print(f'O homem mais velho se chama {nomevelho} e tem {idadevelho} anos.')


































