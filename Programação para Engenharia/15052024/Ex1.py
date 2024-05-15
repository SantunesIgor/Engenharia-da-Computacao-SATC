# Fazer uma função que receba três notas de um aluno e que retorne a média dessas 3 notas.
def media(x, y, z):
    return (x + y + z) / 3

a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
print(media(a, b, c))