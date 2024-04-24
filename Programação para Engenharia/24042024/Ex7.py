# Faça um Programa Python que leia uma lista de 5 números inteiros, mostre a soma dos elementos da lista
from numinp import Numinp as ni

lista = []
for i in range(1, 5): lista.append(ni.verf('Digite um número inteiro: '))
print('A soma dos elementos é:', sum(lista))