# Elabore um programa que leia um número inteiro e indique se o número é primo ou não. Lembrando 
# que os números primos são divisíveis somente por 1 e por ele mesmo. No entanto, o número 1 não é primo.
from numinp import Numinp

num = int(Numinp.numinpcls('Digite o número desejado: '))
if num < 2: resp = False
else:
    divlist = []
    for i in range(1, num+1):
        if num % i == 0:
            divlist.append(i)
    if len(divlist) > 2: resp = False
    else: resp = True
if resp == True: print('É um número primo!')
else: print('Não é um número primo!')