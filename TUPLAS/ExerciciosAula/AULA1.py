# AULA 1 - 02/03

from modulo import *

def exibe_resposta(perimetro):
    moldura(20,'*')
    print(perimetro)
    moldura(20,'*')
    return

xp1 = int(input("X1:"))
yp1 = int(input("Y1:"))
xp2 = int(input("X2:"))
yp2 = int(input("Y2:"))
xp3 = int(input("X3:"))
yp3 = int(input("Y3:"))

perimetro= calc_perimetro(xp1, yp1, xp2, yp2, xp3, yp3)
exibe_resposta(perimetro)