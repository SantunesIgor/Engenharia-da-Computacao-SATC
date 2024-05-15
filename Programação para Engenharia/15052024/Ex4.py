# Elabore uma função que recebe como entrada um número inteiro positivo n e retorne a soma de 
# todos os inteiros positivos menores ou iguais a n.
def func(n):
    a = 0
    for i in range(0, n + 1): a = a + i
    return a

print(func(1))
print(func(5))
print(func(10))