#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
print(f'O produto vale R${preco} e com 5% de desconto ele fica R${preco - (preco*5/100):.2f}')
