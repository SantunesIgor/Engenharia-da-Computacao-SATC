# Escreva um programa que lido um número, calcule e informe o seu fatorial. 
from numinp import Numinp
import math

ans = int(Numinp.numinpcls('Digite o número desejado: '))
if ans < 0: print('Não há fatorial para números negativos')
else: print(math.factorial(ans))