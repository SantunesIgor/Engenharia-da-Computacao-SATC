'''
Escrever um algoritmo para ler dois valores e escolher a operação 
matemática desejada (adição, subtração, multiplicação e divisão). 
Ao final exibir o resultado.

Exemplo:  valor1 =  2
	    valor2 =  3
               operação = adição
               Resultado = 5
'''
import os

def numinp(s):
    while True:
        try: 
            n = float(input(s))
            os.system('cls')
            break
        except:
            os.system('cls')
            print('Por favor, digite um número válido.')
    return n
    
n1 = numinp('Digite o primeiro número: ')
os.system('cls')
while True:
    ope = input('Digite o operador desejado(+, -, *, /): ')
    if ope not in ['+', '-', '*', '/']:
        os.system('cls')
        print('Por favor, digite um operador válido.')
    else: 
        os.system('cls')
        break

n2 = numinp('Digite o segundo número: ')
match ope:
    case '+': ope = n1 + n2
    case '-': ope = n1 - n2
    case '*': ope = n1 * n2
    case '/': ope = n1 / n2

print('O resultado da sua conta é:', ope)