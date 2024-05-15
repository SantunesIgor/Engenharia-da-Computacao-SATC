# Elabore uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. 
# Caso contrário, retorne False.
def ver(n):
    if n % 400 == 0: print('O Ano é bissexto')
    elif n % 4 == 0 and n % 100 != 0: print('O Ano é bissexto')
    else: print('O Ano não é bissexto')

ver(2024)
ver(2022)
ver(2000)
ver(1900)