'''
Utilizando a linguagem PYTHON, crie 2 listas: uma lista com  nomes dos clientes de um banco (João, 
Maria, etc...) e outra lista com saldo da conta em reais(R$) correspondentes ao cliente (1350, 
3240, etc... ), e usando estruturas de repetição mostre os  dados da seguinte forma:

Nome Cliente		Saldo Conta R$
João			1350,00
Maria			3240,00
Etc.

Mostrar também nome dos clientes com maior e menor saldo da conta.
'''
cliente = ['João', 'Maria', 'Mateus']
saldo = [1350, 3240, 2420]
print('Nome Cliente | Saldo Conta R$')
for i in cliente:
    print(i + ' | ' + str(saldo[cliente.index(i)]))
print('Cliente com mais saldo:', cliente[saldo.index(max(saldo))], '-', max(saldo))
print('Cliente com menos saldo:', cliente[saldo.index(min(saldo))], '-', min(saldo))