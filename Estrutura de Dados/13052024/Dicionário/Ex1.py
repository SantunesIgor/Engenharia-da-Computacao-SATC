# Elabore um script em  linguagem Python, utilizando Dicionários, que contenha 4 funcionários, 
# com o índice numérico e seu nome. Em seguida, solicite do usuário demitir um dos funcionários 
# conforme o número de cadastro e mostre na tela os funcionários restantes.
import os

F = {20314: 'Fernando Rodrigues dos Santos', 20315: 'Gabriela Teixeira Montes', 20316: 'Gustavo dos Anjos Silva', 20317: 'Amanda de Freitas'}

print("Funcionários:")
for i, j in F.items():
    print(f"{i}: {j}")

cad = int(input("Digite o número de cadastro do funcionário a ser demitido: "))
os.system('cls')

if cad in F:
    del F[cad]
    print("Funcionário demitido com sucesso!")
else:
    print("Número de cadastro não encontrado.")

print("Funcionários restantes:")
for i, j in F.items():
    print(f"{i}: {j}")
