'''
Escrever um algoritmo para ler nome e idade de uma pessoa e verificar a classificação:
Idade			Classificação
0..3			 escreva ('Bebê');
4..11			 escreva ('Criança');
12..17 		 	 escreva ('Adolescente');
18..60			 escreva ('Adulto');
61..99			 escreva ('3ª Idade');
'''
import os

while True:
    try: 
        age = float(input("Digite a sua idade: "))
        os.system('cls')
        if age < 0:
            os.system('cls')
            print('A idade mínima possível é 0')
            continue
        break
    except:
        os.system('cls')
        print('Por favor, digite um número válido.')

if age >= 0 and age <= 3: print('Você é um bebe')
elif age > 3 and age <= 11: print('Você é uma criança')
elif age > 11 and age <= 17: print('Você é um adolescente')
elif age > 17 and age <= 60: print('Você é um adulto')
else: print('Você é uma pessoa da 3ª idade')