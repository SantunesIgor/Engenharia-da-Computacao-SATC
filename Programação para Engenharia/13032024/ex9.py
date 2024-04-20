'''
Elabore um programa que leia o nome do usuário e mostre o nome de traz 
para frente, utilizando somente letras maiúsculas.
'''

msg = input("Digite a sua frase: ").upper()[::-1]
print(msg)