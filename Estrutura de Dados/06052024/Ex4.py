'''
Faça um Programa Python que leia uma frase (caracteres), e diga quantas vogais e 
consoantes foram lidas. Mostre a lista ao final.
'''
chars = input('Digite uma frase: ')
vogal = 0
consoante = 0
for i in chars:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']: vogal += 1
    else: consoante += 1
print(f'Consoantes: {consoante}\nVogais: {vogal}\n{chars}')