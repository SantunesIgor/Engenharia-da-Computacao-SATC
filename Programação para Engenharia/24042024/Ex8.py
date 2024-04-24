# Faça um Programa Python que peça a idade de 10 pessoas, armazene  a informação na sua 
# respectiva lista. Imprima a lista das idades na ordem menor para maior
from numinp import Numinp as ni

lista = []
for i in range(0, 10): lista.append(ni.vintnat('Digite a idade: '))
lista.sort()
print(lista)