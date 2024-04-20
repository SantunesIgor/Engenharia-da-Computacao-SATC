'''
Construir um algoritmo para cadastrar os dados de um funcionário, a partir 
dos dados de entrada: nome, cargo e salário. 
Sigla	Cargo		
T		Técnico		
E		Engenheiro de Software
A		Analista Sistemas
P		Programador
W		Web-Designer
G		Gerente Projetos
'''
import os

nam = input('Digite o seu nome: ')
os.system('cls')
while True:
    pos = input('T - Técnico(a)\nE - Engenheiro de Software(a)\nA - Analista de Sistemas\nP - Programador(a)\nW - Web Designer\nG - Gerente de Projetos\nDigite o seu cargo: ').lower()
    if len(pos) == 1 and pos in ['t', 'e', 'a', 'p', 'w', 'g']: 
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Por favor, digite um caractere válido!')

match pos:
    case 't': pos = 'Técnico(a)'
    case 'e': pos = 'Engenheiro(a) de Software'
    case 'a': pos = 'Analista de Sistemas'
    case 'p': pos = 'Programador(a)'
    case 'w': pos = 'Web Designer'
    case 'g': pos = 'Gerente de Projetos'

while True:
    try:
        wag = float(input("Digite o seu salário: "))
        os.system('cls')
        break
    except: 
        os.system('cls')
        print('Por favor, digite um número válido!')

print('Você é %s, trabalha como %s e ganha %.2f' %(nam, pos, wag))