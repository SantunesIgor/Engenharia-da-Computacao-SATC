import os
'''
Crie um programa que peça um valor e imprima na tela se o valor é positivo, negativo ou ainda igual a zero.
'''
while True:
    try:
        val = int(input('Digite o valor: '))
        break
    except:
        os.system('cls')
        print('Por favor, digite um número válido')
if val > 0: print('O número é positivo.')
elif val < 0: print('O número é negativo.')
else: print('O número é 0')
    