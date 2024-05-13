# 2) Crie um dicionário com os nomes dos estados do Brasil e sua respectiva capital, seguindo o exemplo:

# estados = {"Acre" : "Capital Rio Branco",  "Alagoas" :  "Capital Maceió", 
#                     "Amazonas": "Capital Manaus",  "Bahia" : "Capital Salvador", 
#                     "Distrito Federal" : "Capital Brasília",  "Santa Catarina" : "Capital Florianópolis", 
#                     "Rio Grande do Sul" : "Capital Porto Alegre",
#                     "Paraná" : "Capital Curitiba", "São Paulo" : "Capital São Paulo",
#                     "Minas Gerais" : "Cuiabá", "Rio de Janeiro" : "Rio de Janeiro",
#                     "Tocantins": "Capital Palmas"}

# Agora, inclua um novo estado e sua capital no final da lista.
# Mostre em qual posição está "Distrito Federal". 
# Altere a capital do estado "Minas Gerais" para "Belo Horizonte"
# Ao final, mostre a lista completa de séries. 

estados = {"Acre" : "Capital Rio Branco",
            "Alagoas" :  "Capital Maceió", 
            "Amazonas": "Capital Manaus",
            "Bahia" : "Capital Salvador", 
            "Distrito Federal" : "Capital Brasília",
            "Santa Catarina" : "Capital Florianópolis", 
            "Rio Grande do Sul" : "Capital Porto Alegre",
            "Paraná" : "Capital Curitiba",
            "São Paulo" : "Capital São Paulo",
            "Minas Gerais" : "Cuiabá",
            "Rio de Janeiro" : "Rio de Janeiro",
            "Tocantins": "Capital Palmas"}

print(f"Dicionário 'estados' inicialmente: ")
for i, j in estados.items():
    print(f"{i}: {j}")

estados[input('Digite ')]

print(f"\n'Distrito Federal' está na posição: {list(estados.keys()).index('Distrito Federal')}")

estados["Minas Gerais"] = 'Belo Horizonte'
print(f"\nDicionário 'estados' com as capitais corretas: ")
for i, j in estados.items():
    print(f"{i}: {j}")

print(f"\nDicionário 'estados' final: ")
for i, j in estados.items():
    print(f"{i}: {j}")
