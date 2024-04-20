a = float(input('Digite a primeira nota do aluno: '))
b = float(input('Digite a segunda nota: '))
if (a+b)/2 >= 6:
    c = 'aprovado'
else:
    c = 'reprovado'
print('A média das notas do aulo é de: ', (a+b)/2, '\nSituação: ', c)