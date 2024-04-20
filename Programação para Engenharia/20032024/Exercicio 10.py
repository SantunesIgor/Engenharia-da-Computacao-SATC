'''
Crie um programa em Python para calcular a média de três notas inseridas pelo usuário e 
dar feedback baseado na média calculada.

Peça ao usuário para inserir as notas de três avaliações.
Calcule a média das notas e arredonde-a para duas casas decimais.
Exiba a média na tela.
Dê um dos seguintes feedbacks de acordo com a média:
Média maior ou igual a 7.0: "Parabéns! Sua média é alta."
Média maior ou igual a 5.0: "Sua média é razoável."
Média abaixo de 5.0: "Sua média é baixa. É uma boa oportunidade para melhorar.".
'''
import os

def numinp(s):
    while True:
        try: 
            n = float(input(s))
            os.system('cls')
            if n > 10 or n < 0:
                print('Digite uma nota válida')
                continue
            break
        except:
            os.system('cls')
            print('Por favor, digite um número válido.')
    return n

n1 = numinp('Digite a sua primeira nota: ')
n2 = numinp('Digite a sua segunta nota: ')
n3 = numinp('Digite a sua terceira nota: ')
med = (n1 + n2 + n3)/3

print('A sua média final é %.2f' %(med))
if med >= 7: print('Parabéns! Sua média é alta.')
elif med >= 5: print("Sua média é razoável.")
else: print("Sua média é baixa. É uma boa oportunidade para melhorar.")