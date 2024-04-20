# Escreva um programa que leia 10 valores inteiros e encontre o maior e o menor deles.
from numinp import Numinp

list = []
print('Digite os 10 números desejados: ')
for i in range(1, 11):
    ans = Numinp.numinp('')
    list.append(ans)
print('O maior número digitado é: %.2f' %(max(list)))
print('O menor número digitado é: %.2f' %(min(list)))