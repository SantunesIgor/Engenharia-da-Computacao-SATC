'''
Faça um Programa Python que leia uma sequencia de números inteiros e armazene-os numa lista. 
Armazene os números pares na lista PAR e os números impares na lista IMPAR. Imprima ao final 
as listas armazenadas.
'''
nums = input('Digite os números: ')
par = []
impar = []
for i in nums:
    if int(i) % 2 == 0: par.append(i)
    else: impar.append(i)
print(f'Par: {par}\nÍmpar: {impar}')