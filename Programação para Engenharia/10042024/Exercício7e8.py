# Para construir o programa a seguir, considere que os usuários só informarão números inteiros 
# positivos. Crie um programa que receba 10 números digitados e exiba todos os números pares e ímpares.
import os

list = []
for i in range(1, 11):
    ans = int(input('Digite um dos números: '))
    os.system('cls')
    list.append(ans)
listp, listi = [], []
for i in list:
    if i % 2 == 0: listp.append(i)
    else: listi.append(i)
print('Os número pares são:', str(listp))
print('Os números ímpares sao:', str(listi))