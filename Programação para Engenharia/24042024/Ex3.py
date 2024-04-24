# Faça um Programa Python que leia 4 notas, ao final mostre as notas e a média geral
from numinp import Numinp as ni

lista = []
for i in range(1, 5): lista.append(ni.vfloatnat('Digite uma das notas: '))
print('Notas:', lista, '\nA média é:', sum(lista) / len(lista))