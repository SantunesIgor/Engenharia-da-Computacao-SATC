# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;       Idade: entre 0 e 100;
# Salário: maior que zero;                    Sexo: ‘F' ou ‘M';
# Estado Civil: ‘S', ‘C’, ‘V', ‘D';
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salario: '))
sexo = input('Digite seu sexo(F ou M): ').upper()
estadocivil = input('Digite seu estado civil(S, C, V, D): ').upper()
if len(nome) <= 3: print('O nome deve ser maior que 3 letras')
if idade < 0 or idade > 100: print('A idade deve ser entre 0 e 100 anos')
if salario < 0: print('O salario não pode ser negativo')
if sexo not in ['F', 'M']: print('O sexo só pode ser F o M')
if estadocivil not in ['S', 'C', 'V', 'D']: print('O estado civil só pode ser S, C, V ou D')