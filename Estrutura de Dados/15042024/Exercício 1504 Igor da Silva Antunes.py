from collections import deque
import os

fila = deque()

while True:
    print('''1 - Fazer Pedido
2 - Processar Pedido
3 - Mostrar Pedidos''')

    opcao = input("Digite o número da opção escolhida: ")

    match opcao:
        case '1':
            os.system('cls')
            fila.append(input("Digite o pedido: "))
            print("Pedido adicionado à fila.")
        case '2':
            os.system('cls')
            if fila:
                print('Pedido a ser processado:', fila[0])
                if input("O pedido foi completo (se sim digite 'OK'):").lower() == 'ok':
                    fila.popleft()
                    if fila:
                        print('Próximo pedido:', fila[0])
                    else: print("Não há mais pedidos.")
                else: print("Pedido não processado.")
            else: print("Não há mais pedidos.")
        case '3':
            os.system('cls')
            if fila: print("Pedidos pendentes:", list(fila))
            else:
                os.system('cls')
                print("Não há mais pedidos.")
        case _:
            os.system('cls')
            print("Opção inválida. Por favor, escolha uma opção válida.")