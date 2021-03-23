import os

class View:

    def mostrar_mensgem(self, msg):
        print('#'*(round(len(msg)/2)*5))
        print(' '*round(len(msg)/2) + msg)
        print('#'*(round(len(msg)/2)*5))
        pass

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    def escolhas(self, a, b, c, d):
        print('1 - ' + a)
        print('2 - ' + b)
        print('3 - ' + c)
        print('4 - ' + d)
        pass
