# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


# def generarPI(n):
#     PI = 0
#     for _ in xrange(n):
#         U = random.random() # U ~ U(0, 1)
#         V = random.random() # V ~ U(0, 1)
#         X = 2*U - 1 # X ~ U(-1, 1)
#         Y = 2*V - 1 # Y ~ U(-1, 1)

#         # Punto cae adentro del circulo de radio 1
#         if X**2 + Y**2 <= 1:
#             PI += 1

#     PI = 4 * PI/float(n) # PI = 4 * PI/4

#     return PI


def generarPI():
    PI = 0
    U = random.random() # U ~ U(0, 1)
    V = random.random() # V ~ U(0, 1)
    X = 2*U - 1 # X ~ U(-1, 1)
    Y = 2*V - 1 # Y ~ U(-1, 1)

    # Punto cae adentro del circulo de radio 1
    if X**2 + Y**2 <= 1:
        PI += 1

    PI = 4 * PI

    return PI


def estimacion():
    """
    Ejercicio 3.
    """
    n = 1 # Simulaciones
    X = generarPI()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    while n/1536.64 >= S_cuadrado:
        n += 1
        for j in xrange(2, n+1):
            X = generarPI()
            A = M
            M += (X - M)/float(j)
            S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral (sigma)

    IC = (M - 1.96*(S/math.sqrt(n)) , M + 1.96*(S/math.sqrt(n)))

    return IC, n


IC, n = estimacion()
print "\nIntervalo de Confianza (IC) =", IC
print "Ejecuciones Necesarias =", n
print ""
