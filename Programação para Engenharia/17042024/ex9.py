# Faça um script em Python que leia nome, a altura e o sexo de 50 pessoas, após calcule 
# e mostre o seu peso ideal, utilizando as seguintes fórmulas:   
# para homens: ((72.7 * altura) – 58) 
# para mulheres: ((62.1 * altura) - 44.7)
# Ao final exibir o total pessoas de cada sexo (M/F)
from numinp import Numinp as ni

listanome = []
listaalt = []
listasex = []
for i in range(1, 51):
    listanome.append(ni.numinp('Digite o seu nome: '))
    listaalt.append(ni.numinp('Digite a sua altura: '))
    sex = input('Digite o seu sexo(M/F): ')
    listasex.append(ni.numinp('Digite o seu sexo(M/F): '))
print('O peso ideal de cada um é:')
for i in range(1, 51):

    print('%s: %.2f' )