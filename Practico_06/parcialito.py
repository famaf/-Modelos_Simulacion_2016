# -*- coding: utf-8 -*-

import random
import math


def integral():
    """
    Genera un valor X de la integral con el Metodo de Monte Carlo.
    """
    y = random.random()
    X = math.exp(-y/2.0)

    return X


def monteCarlo():
    """
    Ejercicio de Parcialito.
    """
    n = 100 # Minimo numero de simulaciones
    N = n # Simulaciones realizadas
    X = integral()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = integral()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que: S/sqrt(j) < 0.001
    while math.sqrt(S_cuadrado/float(j)) > 0.001:
        N += 1
        j += 1
        X = integral()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

    return M, S, N


def evaluar():
    M, S, N = monteCarlo()
    print "Integral = ", M


evaluar()
