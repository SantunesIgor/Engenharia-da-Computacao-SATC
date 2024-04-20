import os

while True:
    est = input('''C - Casado(a)
S - Solteiro(a)
V - Viúvo(a)
Digite a letra conforme o seu estado civil:''').upper()
    if est in ['C', 'S', 'V']: 
        os.system('cls')
        break
    else: 
        os.system('cls')
        print('Por favor, digite um caractere válido!')
match est:
    case 'C': print('Você é casado(a)')
    case 'S': print('Você é solteiro(a)')
    case 'V': print('Você é viúvo(a)')
