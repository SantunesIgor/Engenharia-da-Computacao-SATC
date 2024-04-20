# Faça um script em Python par ler o nome e  idade de 10 pessoas e  verificar 
# total de pessoas maior e total menor de idade.
from numinp import Numinp as ni

lista = []
n = 0
p = 0
for i in range(1, 11): lista.append(ni.numinp('Digite um número:'))
for i in lista: 
    if i < 18: n += 1
    else: p += 1
print('Maiores de idade:%i\Menores de idade:%i' %(p, n))