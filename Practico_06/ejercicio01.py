# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


# def mediaMuestral(n, funcion):
#     i = 1
#     X = funcion
#     F = X
#     while i <= n:
#         X = X + (funcion - X)/float(i+1)
#         F += X
#         i += 1
#     return F


# def varianzaMuestral(n, funcion):
#     i = 1
#     S = 0
#     F = S
#     while i <= n:
#         S = (1 - 1/float(i)) * S + (i + 1) * (mediaMuestral(i+1, funcion) - mediaMuestral(i, funcion))**2
#         F += S
#         i += 1
#     return F


def estimacion():
    """
    Ejercicio 1.
    """
    n = 30 # Minimo numero de simulaciones
    N = n # Observaciones Realizadas
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
    # Iteramos hasta que: S/sqrt(j) < 0.1
    while math.sqrt(S_cuadrado/float(j)) > 0.1:
        N += 1
        j += 1
        X = normalEstandar()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

    return M, S, N

a, b, c = 0,0,0
for n in xrange(10000):
    M, S, N = estimacion()
    a += M
    b += S
    c += N

print "Media ==>", a/10000.0
print "DE ==>", b/10000.0
print "N ==>", c/10000.0

# M, S, N = estimacion()
# print "\nMedia Muestral =", M
# print "Desviacion Estandar Muestral =", S
# print "Ejecuciones Necesarias =", N
# print ""
