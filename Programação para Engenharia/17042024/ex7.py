# Faça um script em Python que receba dois números e gere os números que estão no 
# intervalo compreendido por eles. Mostre no final a soma dos números.
from numinp import Numinp as ni

n1 = int(ni.numinp('Digite o primeiro número: '))
n2 = int(ni.numinp('Digite o segundo número: '))
if n1 < n2: 
    for i in range(n1 + 1, n2): print(i)
else:
    for i in range(n2 + 1, n1): print(i)