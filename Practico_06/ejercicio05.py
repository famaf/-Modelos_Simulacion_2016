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

    return float(PI)


def estimacion():
    """
    Ejercicio 5.
    """
    n = 30 # Minimo numero de simulaciones
    N = n # Observaciones Realizadas
    X = generarPI() # X ~ N(0, 1)
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que: (2*1.96*S)/sqrt(j) < 0.1
    while True:
        N += 1
        j += 1
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)
        
        S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

        IC = (M - 1.96*(S/math.sqrt(j)) , M + 1.96*(S/math.sqrt(j)))
        if IC[1] - IC[0] < 0.1:
            break
    print IC[1] - IC[0]
    return IC, N


IC, N = estimacion()
print "Intervalo de Confianza 2 (IC) =", IC, "n =", N
