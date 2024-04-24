# Faça um Programa Python que leia uma lista de 10 números inteiros e mostre-os na ordem inversa.
from numinp import Numinp as ni

lista = []
for i in range(1, 11): lista.append(ni.verf('Digite um número inteiro: '))
lista.reverse()
print(lista)