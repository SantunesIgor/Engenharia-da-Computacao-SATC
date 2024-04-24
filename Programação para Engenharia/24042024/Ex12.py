# Crie um script em linguagem Python que leia dois vetores com 5 elementos cada. Gere um terceiro 
# vetor de 10 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois 
# outros vetores. Exibir na tela todos os vetores em linhas separadas
fstlist = []
for i in range(0, 5): fstlist.append(input('Digite um elemento a ser adicionado na primeira lista: '))
scdlist = []
for i in range(0, 5): fstlist.append(input('Digite um elemento a ser adicionado na segunda lista: '))
print(fstlist + scdlist)