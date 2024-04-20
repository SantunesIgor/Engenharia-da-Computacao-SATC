# Desenvolva um script Python onde o usuário necessita digitar a senha de um cofre, 
# esta senha é numérica (987654), enquanto os valores digitais não forem corretos, 
# o programa deverá pedir novamente informando que o valor está incorreto, assim que 
# estiver correto, informar “cofre aberto”.
from numinp import Numinp as ni
import os

while True:
    resp = ni.numinpcls('Digite a senha do cofre: ')
    if resp != 987654:
        os.system('cls')
        print('Senha incorreta')
    else: break
print('Cofre aberto')