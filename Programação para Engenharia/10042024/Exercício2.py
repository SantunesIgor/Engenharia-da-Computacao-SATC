# Escrever um programa que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos.
from numinp import Numinp

list = []
print('Digite os 10 números desejados: ')
for i in range(1, 11):
    ans = Numinp.numinp('')
    list.append(ans)
print('A soma dos 10 números é %.2f' %(sum(list)))