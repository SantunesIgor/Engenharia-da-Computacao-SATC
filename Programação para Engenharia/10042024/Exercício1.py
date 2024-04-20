# Escrever um programa que imprima a tabuada de um número informado pelo usuário.
from numinp import Numinp

ans = Numinp.numinpcls('Digite o número desejado: ')
for i in range(1, 11): print(ans * i)