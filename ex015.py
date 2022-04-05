#programa pergunta a quantidade de km rodados,
#QUANTIDADE DE DIAS ALUGADO
#calcule o prreço sabendo que aluguel 6.0 dia
#e 0.15 por km rodado
qkm = float(input('quantos km o carro rodou? :'))
qda = float(input('quantos dias o carro ficou alugado :'))
tqda = qda*60
tqkmr = qkm*0.15
print('o total pela km é de R$: {} o total por dias alugados é de R$: {} e o total a pagar é de R$: {}'.format(tqkmr, tqda, tqkmr+tqda ))


