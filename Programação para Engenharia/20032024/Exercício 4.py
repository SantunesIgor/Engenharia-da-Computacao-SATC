'''
Escreva um programa que verifique se uma letra digitada é vogal ou consoante. 
Ou ainda se não está nestes grupos.
'''
import os

while True:
    cha = input('Digite a sua letra: ').lower()
    if len(cha) != 1:
        os.system('cls')
        print('Por favor, digite um caractere válido!')
    else: break

if cha in ['a', 'e', 'i', 'o', 'u']: cha = 1

match cha:
    case 1: print('O caractere digitado foi uma vogal.')
    case _: print('O caractere digitado foi uma consoante.')