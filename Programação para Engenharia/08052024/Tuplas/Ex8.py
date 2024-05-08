# Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 
# 1 e na prova 2, respectivamente. Escreva um script em linguagem Python que calcule a média da turma 
# nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média. 

# Exemplo: 
# Tamanho da turma: 5 
# P1 = ( 7.0   8.3   10.0   6.5   9.3)        P2 = ( 8.5   6.9   5.0   7.5   9.8 )

# Resposta: 
# Média da turma na prova 1: 8.22 
# Média da turma na prova 2: 7.54 
# A turma obteve a melhor média na prova 1.
import bi, os
p1 = []
p2 = []
t = tuple(range(0, bi.betterinput('intcls', 'Digite o tamanho da turma: ', 'Número não aceito')))
for i in t:
    p1.append(bi.betterinput('flt', 'Digite a nota: ', 'Número não aceito'))
p1 = tuple(p1)
os.system('cls')
for i in t:
    p2.append(bi.betterinput('flt', 'Digite a nota: ', 'Número não aceito'))
p2 = tuple(p2)
os.system('cls')
print(f'Média da turma na prova 1: {sum(p1) / len(p1)}\nMédia da turma na prova 2: {sum(p2) / len(p2)}')
