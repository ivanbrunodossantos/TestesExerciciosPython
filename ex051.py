# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. /
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão: '))
ordem = termo + 10 * razao
for c in range(termo, ordem, razao):
    print(f'{c}', end=' -> ')
print('Finalizado.')
