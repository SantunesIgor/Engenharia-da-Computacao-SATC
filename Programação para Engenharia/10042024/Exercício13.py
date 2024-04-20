# Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa 
# que auxilie os seus eletricistas no cálculo das principais grandezas da eletricidade que são: Tensão
# , Resistência e Corrente. Sabe-se que U=Ri, onde, U é a Tensão (em V), R é a Resistência (em Ώ) e i 
# a Corrente (em A).

# Você foi contratado(a) pela empresa para atender a essa solicitação. Construa um programa que apresente 
# o seguinte menu:

# # ************************************************
# # CÁLCULO DE GRANDEZAS ELÉTRICAS
# # ************************************************
# # 1. Tensão (em Volt)
# # 2. Resistência (em Ohm)
# # 3. Corrente (em Ampére)
# # ************************************************

# # Qual grandeza deseja calcular?

# Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas 
# para realizar o cálculo. Quando o eletricista escolher:

# a. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente
# b. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente
# c. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência

# Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
from numinp import Numinp

menu = ('''************************************************
CÁLCULO DE GRANDEZAS ELÉTRICAS
************************************************
1. Tensão (em Volt)
2. Resistência (em Ohm)
3. Corrente (em Ampére)
************************************************
''')

print(menu)
opc = Numinp.numinpcls('Digite qual grandeza deseja calcular: ')
match opc:
    case 1:
        res = Numinp.numinpcls('Digite a resistência(em Ohm): ')
        cor = Numinp.numinpcls('Digite a corrente(em Ampére): ')
        print('A tensão do sistema é de:', res * cor)
    case 2:
        ten = Numinp.numinpcls('Digite a tensão(em Volt): ')
        cor = Numinp.numinpcls('Digite a corrente(em Ampére): ')
        print('A tensão do sistema é de:', ten / cor)
    case 3:
        res = Numinp.numinpcls('Digite a resistência(em Ohm): ')
        ten = Numinp.numinpcls('Digite a tensão(em Volt): ')
        print('A tensão do sistema é de:', ten / res)
    case _: print('A opção digitada não existe')