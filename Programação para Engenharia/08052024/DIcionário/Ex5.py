# Desenvolva um script em linguagem Python, utilizando Dicionários, que solicite ao usuário inserir 
# o nome de 10 amigos e seus telefones e os mostre na tela.
d = {}
for i in range(0, 10):
    nome = input('Digite o nome do amigo: ')
    d[nome] = input('Digite o número de telefone: ')
for i, j in d.items():
    print(f'{i}: {j}')