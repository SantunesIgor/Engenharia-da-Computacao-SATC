'''
Faça um Programa Python que crie 3 listas: uma lista com  nomes de frutas (laranja, banana, etc...) 
e outra lista com quantidade em estoque correspondente as frutas (35,20, etc.) e uma terceira lista 
correspondendo o preço do quilo da fruta (4.25,  3,75, etc.) usando estruturas de repetição mostre os 
dados da seguinte forma:

Fruta		Qtde Estoque		Preço Kg
Laranja		35			4.25
Banana		20			3.75
Etc.

Mostrar também as frutas com maior e menor quantidade em estoque.
Mostrar a soma total das quantidades das frutas.
'''
frutas = ['laranja', 'banana', 'maçã']
estoque = [35, 20, 40]
rskg = [4.25,  3.75, 3.05]

print('Fruta | Qtde Estoque | Preço Kg')
for i in frutas:
    print(i + ' | ' + str(estoque[frutas.index(i)]) + ' | ' + str(rskg[frutas.index(i)]))
print('Fruta com maior quantidade em estoque:', frutas[estoque.index(max(estoque))], '-', max(estoque))
print('Fruta com menor quantidade em estoque:', frutas[estoque.index(min(estoque))], '-', min(estoque))
