# Faça um Programa Python que leia 20 números inteiros e armazene-os numa lista. 
# Armazene os números pares na lista PAR e os números impares na lista IMPAR. Imprima 
# ao final os três vetores.
from numinp import Numinp as ni

lista = []
listapar = []
listaimpar = []
for i in range(1, 21): lista.append(ni.verf('Digite um número inteiro: '))
for i in lista:
    if i % 2 == 0: listapar.append(i)
    else: listaimpar.append(i)
print('Lista: {}\nLista PAR: {}\nLista IMPAR: {}'.format(lista, listapar, listaimpar))
