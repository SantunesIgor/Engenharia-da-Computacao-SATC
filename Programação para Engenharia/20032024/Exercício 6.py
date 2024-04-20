'''
Escrever um algoritmo para ler o nome de um aluno e a media final. Após verificar:
Média < 5 - Aluno Reprovado
Média entre 5 e 7 - Aluno em Recuperação
Média >= 7 - Aluno Aprovado
'''
import os

nam = input('Digite o seu nome: ')
while True:
    try: 
        med = float(input("Digite a sua média final: "))
        os.system('cls')
        if med > 10:
            os.system('cls')
            print('A maior média possível é 10.')
            continue
        break
    except:
        os.system('cls')
        print('Por favor, digite um número válido.')
    
if med < 5: print('Você, %s, está reprovado.' %(nam))
elif med >= 7: print('Você, %s, está aprovado.' %(nam))
else: print('Você, %s, está em recuperação.' %(nam))