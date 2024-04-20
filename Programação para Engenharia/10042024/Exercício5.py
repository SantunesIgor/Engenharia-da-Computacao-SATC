# Desenvolva um script Python que lê vários números positivos via teclado. 
#Quando o número lido for -1, o script deve parar e exibir a soma de todos
#os números positivos inseridos, a média desses números, o menor e o maior número digitado.
from numinp import Numinp

list = []
ans = 0
while ans >= 0:
    list.append(ans)
    ans = Numinp.numinpcls('Digite o número a ser somado: ')
list.remove(list[0])
print('A soma dos números digitados é:', sum(list))
print('A média dos números digitados é:', sum(list)/len(list))
print('O maior dos números digitados é:', max(list))
print('O menor dos números digitados é:', min(list))