# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área/
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros
# quadrados.
alt = float(input('qual a altura da sua parede :'))
lar = float(input('qual a larguira de sua parede? :'))
mqua = alt * lar
print('a sua parede tem: {:.1f} m2'.format(mqua))
print('você precisará de {:.1f} l de tinta para pintar a parede'.format(mqua/2))





