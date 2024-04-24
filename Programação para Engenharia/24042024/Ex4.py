# Faça um Programa Python que leia uma lista de 10 caracteres, e diga quantas 
# vogais e consoantes foram lidas. Mostre a lista ao final.
lista = []
for i in range(1, 11): 
    while True:
        b = input('Digite um caractere: ')
        try: int(b)
        except: 
            if len(b) != 1: print('Digite um caractere válido')
            else: break
    lista.append(b)
v = c = 0
for i in lista:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']: v += 1
    else: c += 1
print('Vogais: %i\nConsoantes: %i' %(v, c))
            