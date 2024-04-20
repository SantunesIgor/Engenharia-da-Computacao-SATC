# Desenvolva um script Python que leia 10 números e informe o maior e menor número lido.
from numinp import Numinp as ni

lista = []
for i in range(1, 11): lista.append(ni.numinp('Digite um número:'))

print('O maior número da lista é:%.2f\nO menor número da lista é:%.2f' %(max(lista), min(lista)))