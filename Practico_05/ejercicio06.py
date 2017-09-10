# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def metodoMax(n):
    """
    Ejercicio 6 con Metodo de Maximo de Uniformes.
    """
    return maxUniformes(n)


def transformadaInversa(n):
    """
    Ejercicio 6 con Metodo de Transformada Inversa.
    """
    u = random.random()
    x = raizGeneral(u, n)

    return x


def aceptacionRechazo(n):
    """
    Ejercicio 6 con Metodo de Aceptacion y Rechazo.
    """
    y = random.random()
    u = random.random()

    while u >= (y**(n-1)):
        y = random.random()
        u = random.random()

    x = y

    return x


def esperanza1(N, n):
    """
    Esperanza con Metodo de Maximo de Uniformes.
    """
    a = 0
    for _ in xrange(N):
        a += metodoMax(n)

    return a/float(N)


def esperanza2(N, n):
    """
    Esperanza con Metodo de Transformada Inversa.
    """
    a = 0
    for _ in xrange(N):
        a += transformadaInversa(n)

    return a/float(N)


def esperanza3(N, n):
    """
    Esperanza con Metodo de Aceptacion y Rechazo.
    """
    a = 0
    for _ in xrange(N):
        a += aceptacionRechazo(n)

    return a/float(N)



print("Metodo de Maximo de Uniformes")
for N in [100, 1000, 10000, 100000]:
    print("N =", N, "n = 10", "--> E(X) =", esperanza1(N, 10))

print("------------------------------")

print("Metodo de Transformada Inversa")
for N in [100, 1000, 10000, 100000]:
    print("N =", N, "n = 10", "--> E(X) =", esperanza2(N, 10))

print("------------------------------")

print("Metodo de Aceptacion y Rechazo")
for N in [100, 1000, 10000, 100000]:
    print("N =", N, "n = 10", "--> E(X) =", esperanza3(N, 10))
