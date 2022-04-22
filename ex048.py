#Faça um programa que calcule a soma entre todos os números que são múltiplos de três /
#e que se encontram no intervalo de 1 até 500.

soma = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        soma = soma + a
        print('A soma dos numeros soliscitados é  {}'.format(soma))




