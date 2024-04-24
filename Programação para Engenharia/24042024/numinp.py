import os

class Numinp:
    def verfcls(s):
        while True:
            try: 
                n = int(input(s))
                os.system('cls')
                break
            except:
                os.system('cls')
                print('Por favor, digite um número válido.')
        return n

    def verf(s):
        while True:
            try: 
                n = int(input(s))
                break
            except:
                print('Por favor, digite um número válido.')
        return n
    
    def vfloatcls(s):
        while True:
            try: 
                n = float(input(s))
                os.system('cls')
                break
            except:
                os.system('cls')
                print('Por favor, digite um número válido.')
        return n


    def vfloat(s):
        while True:
            try: 
                n = float(input(s))
                break
            except:
                print('Por favor, digite um número válido.')
        return n

    def vfloatnat(s):
        while True:
            try: 
                n = float(input(s))
                if n < 0:
                    print('Por favor, digite um número válido.')
                    continue
                break
            except:
                print('Por favor, digite um número válido.')
        return n
    
    def vintnat(s):
        while True:
            try: 
                n = int(input(s))
                if n < 0:
                    print('Por favor, digite um número válido.')
                    continue
                break
            except:
                print('Por favor, digite um número válido.')
        return n