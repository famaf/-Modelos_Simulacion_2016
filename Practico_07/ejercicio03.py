# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def pValor(r, n, d):
    """
    r = Numero de simulaciones
    n = Tamaño de la muestra
    d = Valor observado
    """
    uniformes = []
    valoresD = []
    exitos = 0 # Cantidad de veces que se cumple que D >= d

    for _ in xrange(r):
        # Generamos n U ~ U(0, 1)
        for _ in xrange(n):
            uniformes.append(random.random())
        uniformes.sort()

        # Calculamos el estadistico D correspondiente
        j = 1
        for U in uniformes:
            valoresD.append(j/float(n) - U)
            valoresD.append(U - (j-1)/float(n))
            j += 1

        D = max(valoresD)

        # Si D >= d --> es un exito
        if D >= d:
            exitos += 1

        # Vaciamos las listas: uniformes y valoresD
        uniformes = []
        valoresD = []

    p_valor = exitos/float(r)

    return p_valor


def testKS():
    """
    Test de Kolmogorov-Smirnov.
    Funcion de distribucion acumulada de una U(a, b):
               | 0 si x < a
        F(x) = | (x-a)/(b-a) si a<=x>b
               | 1 si x >= b
    """
    numeros = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    numeros.sort()

    n = len(numeros) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contendra los elementos del conjunto D+ y D-
    j = 1
    for valor in numeros:
        F = valor # Funcion de distribucion acumulada de una U(0,1) -> F(x) = x
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    d = max(valoresD) # Valor observado

    p_valor = pValor(10000, n, d)

    # if p_valor < alfa:
    #     print "Se rechaza H0"
    # elif p_valor > alfa:
    #     print "No se rechaza H0"

    return p_valor



print "p-valor =", testKS()
