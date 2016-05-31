# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def sumaRangos(muestra1, muestra2):
    muestra = muestra1 + muestra2
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos) # Suma de los rangos

    return R


def P(n, m, k):
    """
    Calcula la probabilidad P (dado n, m) de k.
    """
    if n == 1 and m == 0:
        if k <= 0:
            result = 0
        else:
            result = 1
    elif n == 0 and m == 1:
        if k < 0:
            result = 0
        else:
            result = 1
    else:
        if n == 0:
            result = (m/float(m+n)) * P(n, m-1, k)
        elif m == 0:
            result = (n/float(n+m)) * P(n-1, m, k-n-m)
        else:
            result = (n/float(n+m)) * P(n-1, m, k-n-m) + (m/float(m+n)) * P(n, m-1, k)

    return result


def simulacion():
    muestra1 = [65.2, 67.1, 69.4, 78.4, 74, 80.3]
    muestra2 = [59.4, 72.1, 68, 66.2, 58.5]

    # muestra1 = [132, 104, 162, 171, 129]
    # muestra2 = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    R = sumaRangos(muestra1, muestra2)

    p_valor = 2 * min(P(n, m, R), 1 - P(n, m, R-1))

    return p_valor


def simulacion2():
    muestra1 = [65.2, 67.1, 69.4, 78.4, 74, 80.3]
    muestra2 = [59.4, 72.1, 68, 66.2, 58.5]

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    N = n + m

    R = sumaRangos(muestra1, muestra2)

    numerador = R - n*((N+1)/2.0)
    denominador = math.sqrt(n * m * ((N+1)/12.0))

    w = numerador/denominador




print simulacion()
