# Execute um script Python que imprima na tela apenas os números ímpares entre 1 e 50.
from numinp import Numinp as ni

lista = []
for i in range(1, 51): 
    if i % 2 != 0: lista.append(i)
for i in lista: print(i)