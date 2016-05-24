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
    pro = 1/6.0

    lanzamientos = 1000

    valor1 = 158
    valor2 = 172
    valor3 = 164
    valor4 = 181
    valor5 = 160
    valor6 = 165

    N = [valor1, valor2, valor3, valor4, valor5, valor6]
    p = [pro for _ in xrange(6)]

    T = estadistico(6, lanzamientos, N, p)

    grados_libertad = 5

    p_valor = pValor(grados_libertad, T)

    return p_valor


def simulacion(r):
    pass




print "p-valor =", chiCuadrado()
