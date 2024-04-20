import os
'''
Desenvolva um script que solicite dois números quaisquer e mostre o maior entre  eles.
'''
def numinp(s):
    while True:
        try: 
            n = int(input(s))
            os.system('cls')
            break
        except:
            os.system('cls')
            print('Por favor, digite um número válido.')
    return n
    
n1 = numinp('Digite o primeiro número: ')
n2 = numinp('Digite o segundo número: ')
if n1 > n2: print('O número %i maior que o número %i' %(n1, n2))
elif n1 == n2: print('Os números são iguais!')
else: print('O número %i maior que o número %i' %(n2, n1))