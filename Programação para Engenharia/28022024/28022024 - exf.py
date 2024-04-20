# 1)
# pv = float(input("Digite o valor do investimento: "))
# n = float(input('Digite o número de meses em que o valor estará aplicado: '))
# i = float(input('Digite a rentabilidade mensal do investimento (em porcentagem): '))
# fv = pv * pow((1 + (i/100)), n)
# print('O valor do montante final é de: ', fv, "\nSeu lucro foi de: ", fv - pv)

# 2)
# fv = float(input("Digite o valor final desejante: "))
# n = float(input('Digite o número de meses que o valor ficará aplicado: '))
# i = float(input('Qual será a rentabilidade mensal do investimento: '))
# pv = fv/(pow((1 + (i/100)), n))
# print('O valor inicial deverá ser de: %f\nSeu lucro será de %f' %(pv, fv - pv))

# 3) 
a = 24.95 * (1 - 0.35)
n = int(input('Digite quantos livros serão comprados: '))
f = 3 + (n - 1) * 0.75
print('O valor gasto será de: %f\nValor gasto em livros: %f\nValor gasto em frete: %f' %(a * n + f, a * n, f))
