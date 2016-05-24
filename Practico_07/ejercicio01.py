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
    pass




print "p-valor =", chiCuadrado()

