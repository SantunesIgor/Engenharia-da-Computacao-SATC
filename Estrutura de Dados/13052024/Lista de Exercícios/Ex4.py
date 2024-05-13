# 4) Crie um dicionário com os nomes de atletas famosos, seguindo exemplo:

# atletas = { "Cristiano Ronaldo" : "Futebol", "LeBron James" : "Basquete",
#                     "Lionel Messi" : "Futebol", "Neymar" : "Futebol",
#                     "Conor McGregor" : "MMA", "Roger Federer" : "Tênis",
#                      "Rafael Nadal" : "Tênis",  "Stephen Curry" : "Basquete",
#                      "Tiger Woods" : "Golfe",  "Kevin Durant" : "Basquete",
#                       "Lewis Hamilton" : "Fórmula 1", "Sun Yang" : "Natação" }

# Agora, inclua um novo atleta no final da lista 
# Mostre em qual posição está o atleta  "Roger Federer". 
# Infelizmente o atleta "Tiger Woods" não faz mais parte da lista e deve ser removido.
# Ao final, mostre a lista completa de atletas.
import os

atletas = {"Cristiano Ronaldo" : "Futebol",
            "LeBron James" : "Basquete",
            "Lionel Messi" : "Futebol",
            "Neymar" : "Futebol",
            "Conor McGregor" : "MMA",
            "Roger Federer" : "Tênis",
            "Rafael Nadal" : "Tênis",
            "Stephen Curry" : "Basquete",
            "Tiger Woods" : "Golfe",
            "Kevin Durant" : "Basquete",
            "Lewis Hamilton" : "Fórmula 1",
            "Sun Yang" : "Natação" }

for i, j in atletas.items():
    print(f"{i}: {j}")
aux = input('Digite o nome do atleta a ser adicionado: ')
atletas[aux] = input('\nDigite o esporte que ele participa: ')

os.system('cls')
for i, j in atletas.items():
    print(f"{i}: {j}")
aux = input('Digite um atleta para mostrar seu index no dicionário: ')

os.system('cls')
for i, j in atletas.items():
    print(f"{i}: {j}")
print(f"O index do time {aux} é: {list(atletas.keys()).index(aux)}")
del atletas[input('Digite um atleta para ser removido: ')]

os.system('cls')
for i, j in atletas.items():
    print(f"{i}: {j}")