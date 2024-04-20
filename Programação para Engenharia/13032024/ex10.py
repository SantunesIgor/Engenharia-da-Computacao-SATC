'''
Desenvolva um programa que leia uma frase e um caractere. 
Em seguida, exiba ambos e o número de ocorrências do caractere na frase.
'''

msg = input('Digite a sua frase: ')
char = input('Digite o caracter desejado saber a frequência: ')
n = 0
cont = 0
for i in msg: 
    if msg[n] == char:
        cont += 1
    n += 1
print("%s\nO número de ocorrências da letra '%s' na frase acima é de: %s" %(msg, char, cont))