#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o seu salário? R$'))
print(f'Você recebia R${salario:.2f} e com o aumento de 15% você irá receber R${salario + (salario * 15 / 100):.2f}.')
