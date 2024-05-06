'''
Faça um Programa Python que leia a idade das pessoas, armazene  a informação na sua respectiva lista.
Mostre ao final a lista das idades na ordem menor para maior.
'''
import os

ans = ''
idade = []
for i in range(1, 11):
    ans = idade.append(int(input('Digite a idade: ')))
    os.system('cls')
idade.sort()
print('Idades informadas:', idade)