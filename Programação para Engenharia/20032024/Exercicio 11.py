'''
Um posto de abastecimento está comercializando combustíveis com a seguinte tabela de descontos:

Álcool: até 20 litros, desconto de 2% por litro;
	    acima de 20 litros, desconto de 5% por litro;

Gasolina: até 20 litros, desconto de 4% por litro;
	      acima de 20 litros, desconto de 6% por litro;

Desenvolva um programa em Python que leia o número de litros vendidos e o tipo de combustível (codificado 
com A - Álcool e G - Gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo que o litro da 
gasolina está em R$ 5,57 e do álcool R$ 4,98.
'''
import os

while True:
    com = input('A - Álcool\nG - Gasolina\nDigite com oque vai abastecer: ').lower()
    if len(com) == 1 and com in ['a', 'g']: 
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Por favor, digite um caractere válido!')

while True:
    try:
        lit = float(input("Digite quantos litros serão enchidos: "))
        os.system('cls')
        break
    except: 
        os.system('cls')
        print('Por favor, digite um número válido!')


if com == 'a' and lit <= 20: pre = 4.98 * lit * 0.98
elif com == 'a' and lit > 20: pre = 4.98 * lit * 0.95
elif com == 'g' and lit <= 20: pre = 5.57 * lit * 0.96
else: pre = 5.57 * lit * 0.94

print("O valor gasto será de %.3fR$" %(pre))