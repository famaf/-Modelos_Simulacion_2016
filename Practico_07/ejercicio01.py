# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def estadistico(k, n, N, p):
    """
    Calcula el estadistico T.
    k = particiones (intervalos).
    n = tamaño de la muestra.
    N = vector de valores (Frecuencia Observada) de tamaño k.
    p = valores de valores (Frecuencia Esperada) de tamaño k
    """
    T = 0
    for i in xrange(k):
        T += ((N[i] - n*p[i])**2)/float(n*p[i])

    return T


def chiCuadrado():
    p_blanca = 1/4.0
    p_rosa = 1/2.0
    p_roja = 1/4.0

    guisantes = 564

    blancas = 141
    rosas = 291
    rojas = 132

    N = [blancas, rosas, rojas]
    p = [p_blanca, p_rosa, p_roja]

    T = estadistico(3, guisantes, N, p)

    grados_libertad = 2

    p_valor = pValor(grados_libertad, T)

    return p_valor


def simulacion(r):
    n = 50
    k = 5
    t = 12.8
    P = [0.2, 0.2, 0.2, 0.2, 0.2]


    Q = [0.2, 0.4, 0.6, 0.8, 1]

    B = [0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0]
    X = [0, 0, 0, 0, 0]
    for j in xrange(k):
        B[j] = n * P[j]
        C[j] = 1.0/B[j]

    exitos = 0
    for _ in xrange(r):
        for _ in xrange(n):
            u = random.random()
            i = 0

            while u >= Q[i]:
                i += 1

            X[i] += 1

        T = 0

        for l in xrange(k):
            Ti = (X[l] - B[l])**2 * C[l]
            T += Ti

        if T >= t:
            exitos += 1

    return exitos/float(r)





print "p-valor =", chiCuadrado()
print simulacion(1000)
