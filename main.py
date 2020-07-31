import os
from math import pi
from function import *
from interface import *

opem = True

while opem == True:

    print(interface.start)
    print("para entrar nas opções \r")
    os.system("pause")
    print(interface.opção_1,"\n",interface.opção_2, "\n", interface.opção_3)
    numero = int(input())

    if numero == 1:
        calcular_quadrado()
    elif numero == 2:
        calcular_circunferencia()
    elif numero == 3:
        exit()
    elif numero != 1 and numero != 2 and numero != 3:
        print(interface.erro)
        
