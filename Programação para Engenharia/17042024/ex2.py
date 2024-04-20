# Crie um programa em linguagem Python que leia 5 números, informando a 
# quantidade de valores positivos, a quantidade de valores negativos
from numinp import Numinp as ni

lista = []
n = 0
p = 0
for i in range(1, 6): lista.append(ni.numinp('Digite um número:'))
for i in lista: 
    if i < 0: n += 1
    else: p +=1
print('Positivos:%.2f\nNegativos:%.2f' %(p, n))