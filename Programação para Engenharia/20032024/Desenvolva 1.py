import os

'''
Desenvolva um script que solicite nome e idade de uma pessoa e mostre se é  maior ou menor de idade.
'''

name = input("Digite o seu nome: ")
os.system('cls')
while True:
    try:
        age = int(input("Digite a sua idade: "))
        os.system('cls')
        break
    except: 
        os.system('cls')
        print('Por favor, digite um número inteiro!')
if age >= 18: print('Você, %s, é maior de idade.' %(name))
else: print('Você, %s, não é maior de idade.' %(name))