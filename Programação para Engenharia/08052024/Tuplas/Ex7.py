# Dada uma tupla  T  de n valores inteiros, elabore um programa que remova todos os números pares da 
# tupla. Exemplo: 
# Tamanho da Tupla T: 10
# T = (1,2,3, 4, 5, 6, 7, 8, 9, 10)
# Resposta: 1 3 5 7 9
import bi
t2 = []
t = tuple(range(1, bi.betterinput('intcls', 'Digite o tamanho desejado da tupla: ', 'Número não aceito') + 1))
for i in t:
    if i % 2 != 0:
        t2.append(i)
print('Os números ímpares da tupla são:', tuple(set(t) & set(t2)))
