# Faça um Programa Python que leia uma lista com 10 números inteiros, 
# calcule e mostre o maior e menor elemento da lista
from numinp import Numinp as ni

lista = []
for i in range(0, 10): lista.append(ni.verf('Digite um número inteiro: '))
print('Maior elemento: %i\nMenor elemento: %i' %(max(lista), min(lista)))