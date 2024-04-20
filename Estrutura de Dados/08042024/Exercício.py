from collections import deque

expression = input('Digite a sua expressão matemática: ')
stack = deque()
a = 0

for i in expression:
    if i == '(': stack.append(i)
    elif i == ')': 
        try: stack.pop()
        except: 
            a = 1
            break

if not stack and a != 1: print('Está balanceado')
else: print('Não está balanceado')
