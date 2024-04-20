# Crie um programa em linguagem Python que leia 5 números, calcule e mostre a média 
# aritmética dos valores lidos.
from numinp import Numinp as ni

lista = []
for i in range(1, 6): lista.append(ni.numinp('Digite um número:'))
print('A média é', sum(lista)/len(lista))