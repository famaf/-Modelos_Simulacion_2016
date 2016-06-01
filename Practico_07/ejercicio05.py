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


def estimacionP(t, lista):
    """
    Estimacion del valor 'p' en base a una lista de valores.
    Clase: Analisis estadistico de datos simulados. Estimadores puntuales
    Filmina: 16
    """
    media = sum(lista)/float(len(lista))

    p = media/float(t)

    return p


def simulacion():
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()

    p = estimacionP(8, datos) # Estimamos la probabilidad 'p' = 0.62

    n = len(datos) # Tamaño de la muetra



print "p-valor =", estimacion()
