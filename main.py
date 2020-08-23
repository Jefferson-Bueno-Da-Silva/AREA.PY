from os import system
from math import pi
from function import *
from interface import *

opem = True

while opem == True:

    print(interface.start)
    print("para entrar nas opções \r")
    system("pause")
    print(interface.opção_1,"\n",interface.opção_2, "\n", interface.opção_3, interface.opção_4, "\n")
    numero = int(input())

    if numero == 1:
        calcular_quadrado()
    elif numero == 2:
        calcular_circunferencia()
    elif numero == 3:
        calcular_retangulo()
    elif numero == 4:
        exit()
    elif numero != 1 and numero != 2 and numero != 3 and numero != 4:
        print(interface.erro)
        
