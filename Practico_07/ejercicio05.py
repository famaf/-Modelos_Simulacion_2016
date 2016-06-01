# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def estadisticoT(k, n, N, p):
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


def calculoBinomial(n, p, i):
    """
    Funcion de masa de una distribucion Binomial B(n, p)
    """
    combinatorio = math.factorial(n)/float(math.factorial(i) * math.factorial(n-i))

    return combinatorio * p**i * (1 - p)**(n-i)


def simulacion():
    """
    Calculo del p-valor de un conjunto de datos segun la distribucion Binomial.
    """
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()

    # Estimamos la probabilidad 'p' = 0.618
    p = estimacionP(8, datos)

    m = 1 # Cantidad de parametros estimados
    n = len(datos) # Tamaño de la muetra
    k = 9 # Cantidad de intervalos
    # k = 3

    N = [0, 1, 2, 4, 1, 1, 2, 5, 2] # Frecuencias observadas
    # N = [0, 3, 15]

    # Calculamos las 9 probilidades de una B(8, p)
    pro = []
    for i in xrange(9):
        pro.append(calculoBinomial(8, p, i))

    # a = pro[0]
    # b = pro[1] + pro[2]
    # c = pro[3] + pro[4] + pro[5] + pro[6] + pro[7]
    # pro = [a, b, c]

    t = estadisticoT(k, n, N, pro) # Valor observado

    grados_libertad = k - m - 1 # En este caso son 7

    p_valor = pValor(grados_libertad, t)

    return p_valor



print "p-valor =", simulacion()
