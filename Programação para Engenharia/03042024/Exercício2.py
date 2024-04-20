import os

while True:
    print('Será que você pode votar?')
    try:
        idade = int(input("Digite a sua idade(em anos): "))
        os.system('cls')
        if idade < 0:
            print('Por favor, digite uma idade válida')
            continue
        break
    except:
        os.system('cls')
        print('Por favor, digite uma idade válida')
if idade < 16:
    print('Você é proibido de votar (proibido).')
elif idade < 18 or idade >= 65:
    print('Você não é obrigado a votar (optativo).')
elif idade < 65:
    print('Você é obrigado a votar (obrigado).')