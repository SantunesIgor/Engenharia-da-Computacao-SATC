import os

while True:
    try:
        distancia = int(input("Digite a distância da viajem (em km): "))
        os.system('cls')
        if distancia < 0:
            print('Por favor, digite uma distância válida')
            continue
        break
    except:
        os.system('cls')
        print('Por favor, digite uma distância válida')

if distancia <= 200:
    print('O preço da sua viajem será de %.2f, sendo o valor por km de 0.50' %(distancia * 0.50))
else:
    print('O preço da sua viajem será de %.2f, sendo o valor por km de 0.45' %(distancia * 0.45))