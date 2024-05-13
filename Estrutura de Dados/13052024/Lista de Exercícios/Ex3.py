# 3) Crie um dicionário com os nomes de times de futebol de SC, seguindo exemplo:

# times = {1: "Criciuma",  2: "Avai",  3: "Marcilio Dias", 4: "Joinville", 
#                 5: "Figueirense",  6: "Chapecoense",  7: "Brusque", 8: "Metropolitano"
#                 9: "Hercílio Luz", 10: "Inter de Lages" }

# Agora, inclua um novo time no final da lista 
# Mostre em qual posição está o time  "Joinville". 
# Infelizmente o time "Avaí" não fazem mais parte da lista e deve ser removida.
# Ao final, mostre a lista completa de times.
import os

times = {1: "Criciuma",
        2: "Avai",
        3: "Marcilio Dias",
        4: "Joinville", 
        5: "Figueirense",
        6: "Chapecoense",
        7: "Brusque",
        8: "Metropolitano",
        9: "Hercílio Luz",
        10: "Inter de Lages"}

for i, j in times.items():
    print(f"{i}: {j}")
times[11] = input('Digite um time para ser adicionado: ')

os.system('cls')
for i, j in times.items():
    print(f"{i}: {j}")
aux = input('Digite um time para mostrar seu index no dicionário: ')

os.system('cls')
for i, j in times.items():
    print(f"{i}: {j}")
print(f"O index do time {aux} é: {list(times.values()).index(aux)}")
aux = input('Digite um time para ser removido: ')
for i, j in list(times.items()):
    if j == aux:
        del times[i]

os.system('cls')
for i, j in times.items():
    print(f"{i}: {j}")