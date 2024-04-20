# Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: 

# • adição (opção 1) 
# • subtração (opção 2) 
# • multiplicação (opção 3) 
# • divisão (opção 4)
# • saída (opção 5) 

# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a 
# volta ao menu de opções. O programa somente termina quando for escolhida a opção de saída (opção 5).
from numinp import Numinp
import os

opc = 0
menu = ('''Adição(1)
Subtração(2)
Multiplicação(3)
Divisão(4)
Saída(5)''')

while True:
    print(menu)
    while opc not in [1, 2, 3, 4, 5]:
        opc = Numinp.numinp('Digite a opção escolhida: ')
        if opc not in [1, 2, 3, 4, 5]:
            print('Digite um número válido')
    if opc == 5: break
    num1 = Numinp.numinpcls('Digite o primeiro número: ')
    num2 = Numinp.numinpcls('Digite o segundo número: ')
    os.system('cls')
    match opc:
        case 1: print('O resultado da operação é: ', num1 + num2)
        case 2: print('O resultado da operação é: ', num1 - num2)
        case 3: print('O resultado da operação é: ', num1 * num2)
        case 4: print('O resultado da operação é: ', num1 / num2)
    

