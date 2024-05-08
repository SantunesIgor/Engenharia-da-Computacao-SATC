# Desenvolva um script em linguagem Python, utilizando Dicionários, 
# que solicite ao usuário inserir o nome de 05 livros e seus respectivos 
# autores e os mostre na tela.
d = {}
for i in range(0, 5):
    nome = input('Digite o nome do livro: ')
    d[nome] = input('Digite o autor do livro: ')
for i, j in d.items():
    print(f'{i}: {j}')