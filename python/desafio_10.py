#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
valor = float(input('Quanto dinhairo você tem? R$'))
print(f'Com R${valor:.2f} você pode comprar US${valor/5.56:.2f} e €{valor/6.17:.2f}')