# Elabore um script em  linguagem Python, utilizando Dicionários, que contenha 4 funcionários, com o 
# índice numérico e seu nome. Em seguida, solicite do usuário demitir um dos funcionários conforme o 
# número de cadastro e mostre na tela os funcionários restantes.
funcionarios = {'Fabio': 20123, 'Deiverson': 20124, 'Roberta': 20125, 'Carla': 20126}
print("Funcionários atuais:")
for indice, nome in funcionarios.items():
    print(f"Índice: {indice}, Nome: {nome}")
numero_cadastro = int(input("Digite o número de cadastro do funcionário a ser demitido: "))
if numero_cadastro in funcionarios.values():
    for nome, cadastro in list(funcionarios.items()):
        if cadastro == numero_cadastro:
            funcionarios.pop(nome)
    print("Funcionário demitido com sucesso!")
else:
    print("Número de cadastro inválido.")
print("\nFuncionários restantes:")
for indice, nome in funcionarios.items():
    print(f"Índice: {indice}, Nome: {nome}")