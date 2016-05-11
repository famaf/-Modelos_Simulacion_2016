# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def generarM():
    """
    Genera M tq' M = {n : U1 <= U2 <= ... <= Un-1 > Un}
    """
    n = 2
    U = random.random() # Un-1
    Un = random.random() # Un

    while U <= Un:
        n += 1
        U = Un # U pasa a ser Un (nuevo Un-1)
        Un = random.random() # Generamos un nuevo valor Un

    M = n

    return M


def estimacion01():
    """
    Ejercicio 4 con la Generacion de M.
    """
    n = 1000 # Simulaciones
    X = generarM()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarM()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral (sigma)

    IC = (M - 1.96*(S/math.sqrt(n)) , M + 1.96*(S/math.sqrt(n)))

    return M, S_cuadrado, IC


def estimacion02():
    """
    Ejercicio 4 con la Poisson.
    """
    n = 1000 # Simulaciones
    X = math.e * poisson(1)
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = math.e * poisson(1)
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral (sigma)

    IC = (M - 1.96*(S/math.sqrt(n)) , M + 1.96*(S/math.sqrt(n)))

    return M, S_cuadrado, IC


def puntoC(n):
    a = 0
    for _ in xrange(n):
        a += poisson(1)
    
    return math.e *(a/float(n))


def printEstimacion01():
    M, S_cuadrado, IC = estimacion01()
    print "\nESTIMACION CON LA GENERACION DE M"
    print "### e =", math.e, "###"
    print "Media Muestral =", M
    print "Varianza Muestral =", S_cuadrado
    print "Intervalo de Confianza (IC) =", IC
    print ""


def printEstimacion02():
    M, S_cuadrado, IC = estimacion02()
    print "ESTIMACION CON LA POISSON(1)"
    print "### e =", math.e, "###"
    print "Media Muestral =", M
    print "Varianza Muestral =", S_cuadrado
    print "Intervalo de Confianza (IC) =", IC
    print ""


printEstimacion01()
printEstimacion02()
print "Con Poisson(1) --> E[M] =", puntoC(1000)
