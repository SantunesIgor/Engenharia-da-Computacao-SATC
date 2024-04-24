# Elabore um script em linguagem Python que leia de 10 números reais, inserindo-os numa 
# lista e ao final, mostre-os na ordem inversa.
from numinp import Numinp as ni

lista = []
for i in range(0, 10): lista.append(ni.vfloat('Digite um número: '))
lista.reverse()
print(lista)
