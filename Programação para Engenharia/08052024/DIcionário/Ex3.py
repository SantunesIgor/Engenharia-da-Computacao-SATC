# Desenvolva um script em linguagem Python, utilizando Dicionários, que solicite ao usuário 
# inserir o nome de 05 produtos de papelaria e seus respectivos preços e os mostre na tela.
import bi
d = {}
for i in range(0, 5):
    nome = input('Digite o nome do produto: ')
    d[nome] = bi.betterinput('flt', 'Digite o valor do produto: ', 'Nùmero inválido')
for i, j in d.items():
    print(f'{i}: {j}')