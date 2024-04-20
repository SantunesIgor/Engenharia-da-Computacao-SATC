# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
# usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
import os

while True:
    user = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if senha == user:
        os.system('cls')
        print('Dados iguais, por favos os insira novamente.')
    else: break
