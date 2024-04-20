import os

class Numinp:
    def numinpcls(s):
        while True:
            try: 
                n = float(input(s))
                os.system('cls')
                break
            except:
                os.system('cls')
                print('Por favor, digite um número válido.')
        return n
    
    def numinpclsint(s):
        while True:
            try: 
                n = float(input(s))
                os.system('cls')
                if n < 0: 
                    print('Por favor, digite um número válido.')
                    continue
                break
            except:
                os.system('cls')
                print('Por favor, digite um número válido.')
        return n
    
    def numinp(s):
        while True:
            try: 
                n = float(input(s))
                break
            except:
                print('Por favor, digite um número válido.')
        return n