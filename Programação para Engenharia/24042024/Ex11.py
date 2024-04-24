# Desenvolva um script em linguagem Python que peça as quatro notas de 10 alunos, calcule 
# e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.
from numinp import Numinp as ni
from statistics import mean

namelist = []
averagelist = []
for i in range(0, 10):
    namelist.append(input('Digite o nome do aluno: '))
    templist = []
    for i in (0, 4): templist.append(ni.vfloatnat('Digite uma das notas do aluno: '))
    averagelist.append(mean(templist))
for i in range(0, 10):
    if averagelist[i] >= 7:
        print('{}: {}'.format(namelist[i], averagelist[i]))
