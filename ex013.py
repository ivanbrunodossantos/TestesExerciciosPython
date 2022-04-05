#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 10% de desconto.
p = float(input('digite o preço do produto :'))
desc = p-(p*10/100)
print('o preço do seu produto com 10% de desconto, é de: {}'.format(desc))



