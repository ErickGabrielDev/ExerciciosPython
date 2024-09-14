#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua ârea e a quantidade
#de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma ârea de 2m².
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print(f'Sua parede tem a dimensão de {altura}x{largura} e a sua área é de {area}m². \npara pintar essa parede você precisará de {area/2}L de tinta.')


