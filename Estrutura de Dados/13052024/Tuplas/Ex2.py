# Elabore um script Python para criar duas tuplas A e B com valores numéricos, 
# após criar uma nova tupla  C com os valores da união das tuplas A e B
import os

A = ()
B = ()
C = ()

for i in range(0, int(input('Digite a quantidade de elementos da tupla A: '))):
    os.system('cls')
    A = A + tuple([int(input('Digite o elemento a ser adicionado: '))])
for i in range(0, int(input('Digite a quantidade de elementos da tupla B: '))):
    os.system('cls')
    B = B + tuple([int(input('Digite o elemento a ser adicionado: '))])
print(f'A junção das duas tuplas é {A + B}')