# Faça um Programa Python que leia uma lista de 5 números inteiros e mostre-os no final
from numinp import Numinp as ni

lista = []
for i in range(1, 6): lista.append(ni.verf('Digite um número inteiro: '))
print(lista)