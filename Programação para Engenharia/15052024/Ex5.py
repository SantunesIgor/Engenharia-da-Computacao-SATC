# Desenvolva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a 
# soma dos dois seja maior que um terceiro parâmetro, chamado limite.
def func(a, b, limite):
    if a + b > limite: return True
    else: return False

print(func(5, 5, 5))
print(func(5, 5, 50))