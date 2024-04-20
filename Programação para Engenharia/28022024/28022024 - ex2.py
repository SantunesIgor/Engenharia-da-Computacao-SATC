b = float(input('Digite o comprimento da base (em cm): '))
h = float(input('Digite o valor da altura (em cm): '))
if b == h:
    print('A área do seu quadrado é de: %i cm' %(b * h))
else:
    print('A área do seu retângulo é de: %i cm' %(b * h))