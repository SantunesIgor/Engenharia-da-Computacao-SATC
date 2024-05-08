# Escreva um programa Python que, dados duas tuplas que representam dois conjuntos (A e B), 
# construa uma outra que represente a diferença dos dois conjuntos (A <> B). 
a = ('EL1', 'EL2', 'EL3')
b = ('EL1', 'EL5', 'EL6')
c = tuple(set(a) - set(b))
print(c, type(c))
