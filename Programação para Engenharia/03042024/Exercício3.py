import os

while True:
    try:
        data = input('Digite a data desejada(dia/mes/ano): ').split('/')
        os.system('cls')
        if int(data[0]) < 0 or int(data[0]) > 31:
            print('Por favor, digite um dia válido.')
            continue
        elif int(data[1]) < 0 or int(data[1]) > 12:
            print('Por favor, digite um mês válido.')
            continue
        break
    except: print("Por favor, digite números na data, entre barras '/', dete modo: (dia/mes/ano)")
print('A data digitada está correta!')