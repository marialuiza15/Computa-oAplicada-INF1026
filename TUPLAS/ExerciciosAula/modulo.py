# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:16:48 2026

@author: c2320401
"""
import math

def calc_dist(xp1, yp1, xp2, yp2):
    distancia = math.sqrt((xp2-xp1)**2+(yp2-yp1)**2)
    return distancia
    
def calc_perimetro(xp1, yp1, xp2, yp2, xp3, yp3):
    perimetro = calc_dist(xp1, yp1, xp2, yp2) + calc_dist(xp2, yp2, xp3, yp3) + calc_dist(xp1, yp1,xp3, yp3)
    return perimetro

def moldura(qtd, simb):
    print(qtd*simb)
    return