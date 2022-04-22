#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal/
# e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' BEM-VINDO A LOJA DO IVAN '))
preco = float(input('qual o preço das compras? '))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
opcao = float(input('Digite uma opção: '))
if opcao == 1:
    t1 = preco - (preco * 10 / 100)
    print('o valor das suas compras é de {} com 10% de desconto'.format(t1))
elif opcao == 2:
    t2 = preco - (preco * 5 / 100)
    print('o valor das suas compras é de {} com 5% de desconto'.format(t2))
elif opcao == 3:
    t3 = preco / 2
    print('o valor das suas compras é de {} em 2 x de {}'.format(preco, t3))
elif opcao == 4:
   parc4 = int(input('Digite a quantidade de parcelas: '))
   t4 = preco + (preco / 100 * 20)
   t5 = t4 / parc4
   print('sua compra no total irá custar {} e em {} x de {}'.format(t4, parc4, t5))
