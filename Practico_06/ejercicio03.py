# -*- coding: utf-8 -*-

import random
import math


def generarN():
    """
    Calcula el min{ N : Sn > 1 }
    """
    N = 0 # Uniformes generadas
    Sn = 0 # Acumulador de suma de uniformes
    # Si Sn <= 1 entonces sumamos otro numero aleatorio y aumentamos el N
    while Sn <= 1.0:
        Sn += random.random()
        N += 1

    return N


def estimacion():
    """
    Ejercicio 3.
    """
    n = 1000 # Simulaciones
    X = generarN()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarN()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral (sigma)

    IC = (M - 1.96*(S/math.sqrt(n)) , M + 1.96*(S/math.sqrt(n)))

    return M, S, IC


def printEstimacion():
    M, S, IC = estimacion()
    print "\n### e =", math.e, "###"
    print "Media Muestral =", M
    print "Desviacion Estandar Muestral =", S
    print "Intervalo de Confianza =", IC
    print ""


printEstimacion()
