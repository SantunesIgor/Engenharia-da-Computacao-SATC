'''
Faça um Programa Python que crie 2 listas: uma lista com  modelos de veículos (fiat palio, ford fiesta, etc...) e outra lista com o ano correspondente aos veículos (2020, 2021, etc.) usando estruturas de repetição mostre os  dados da seguinte forma:

Veículo		Ano
Fiat Palio	2020
Ford Fiesta	2021
Etc.

Mostrar também os veículos com maior e menor ano.
Mostrar o primeiro e último veículo cadastrado.
Mostrar a quantidade de veículos cadastrados.
'''
modelo = ['fiat palio', 'ford fiesta', 'renault clio']
ano = [2020, 2021, 2001]
print('Modelo | Ano')
for i in modelo:
    print(i + ' | ' + str(ano[modelo.index(i)]))
print('Modelo mais novo:', modelo[ano.index(max(ano))], '-', max(ano))
print('Modelo mais antigo:', modelo[ano.index(min(ano))], '-', min(ano))
print('Primeiro veicúlo cadastrado:', modelo[0])
print('Último veicúlo cadastrado:', modelo[-1])
print('Quantidade de veículos cadastrados:', len(modelo))