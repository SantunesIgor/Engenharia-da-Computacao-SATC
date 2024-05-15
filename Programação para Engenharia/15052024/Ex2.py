# Agora, faça uma função de acordo com a média da função anterior informe o status do aluno 
# de acordo com a tabela a seguir: 

# Nota acima de 6: “Aprovado”;
# Nota entre 4 e 6 :“Verificação Suplementar”; 
# Nota abaixo de 4 : “Reprovado.
def media(x, y, z):
    return (x + y + z) / 3

def status(a):
    if a > 6: print('Aprovado')
    elif a < 4: print('Reprovado')
    else: print('Verificação Suplementar')

a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
a = media(a, b, c)
status(a)