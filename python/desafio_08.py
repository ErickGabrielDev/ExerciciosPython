#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
medida = float(input('Digite um número: '))
print(f'A medida de {medida}m corresponde a {medida*100:.0f}c e {medida*1000:.0f}mm')