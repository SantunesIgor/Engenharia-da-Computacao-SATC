# Crie uma função que recebe como entrada uma lista de números e retorna True se um número 
# passado como parâmetro está presente na lista.

def func(lista, n):
    if n in lista: return True
    else: return False

lista = [1, 2, 3]
print(func(lista, 3))
print(func(lista, 4))
