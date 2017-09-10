# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *

# Conviene generar al menos 100 datos para normalidad de Xbarra y disminuir la
# varianza de S

def estimacion():
    """
    Ejercicio 1.
    """
    n = 30 # Minimo numero de simulaciones
    N = n # Simulaciones realizadas
    X = normalEstandar() # X ~ N(0, 1)
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = normalEstandar()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que: S/sqrt(j) < 0.1 --> 0.1 = d "error"
    while math.sqrt(S_cuadrado/float(j)) > 0.1:
        N += 1
        j += 1
        X = normalEstandar()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

    return M, S_cuadrado, N


def promedioMSN():
    n = 10000
    a, b, c = 0, 0, 0

    for n in xrange(n):
        M, S_cuadrado, N = estimacion()
        a += M
        b += S_cuadrado
        c += N

    proM = a/float(n)
    proS_cuadrado = b/float(n)
    proN = c/float(n)

    return proM, proS_cuadrado, proN


def printEstimacion():
    M, S_cuadrado, N = estimacion()
    print("\nMedia Muestral =", M)
    print("Varianza Muestral =", S_cuadrado)
    print("Ejecuciones Necesarias =", N)
    print("")


def printPromedioMSN():
    proM, proS_cuadrado, proN = promedioMSN()
    print("Promedio Media Muestral =", proM)
    print("Promedio Varianza Estandar =", proS_cuadrado)
    print("Promedio Observaciones =", proN)
    print("")


printEstimacion()
printPromedioMSN()
