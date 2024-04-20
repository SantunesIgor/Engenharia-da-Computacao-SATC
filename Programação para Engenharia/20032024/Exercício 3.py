'''
Elabore um programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino ou Sexo Não Informado.
'''
sex = input('''F - Feminino
M - Masculino
Digite o seu sexo: ''').upper()
match sex:
    case 'F': print('Você é do sexo feminino.')
    case 'M': print('Você é do sexo masculino.')
    case _: print('Você não informou seu sexo.')