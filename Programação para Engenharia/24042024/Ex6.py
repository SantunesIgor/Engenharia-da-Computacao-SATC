# Faça um Programa Python que peça as duas notas de 10 alunos e armazene numa lista. 
# Calcule e mostre a média de cada aluno
from numinp import Numinp as ni
from statistics import mean

namelist = []
averagelist = []
for i in range(0, 10):
    namelist.append(input('Digite o nome do aluno: '))
    templist = []
    for i in (0, 2): templist.append(ni.vfloatnat('Digite uma das notas do aluno: '))
    averagelist.append(mean(templist))
for i in range(0, 10):
    print('{}: {}'.format(namelist[i], averagelist[i]))