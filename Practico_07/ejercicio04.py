# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def acumuladaExponencial(x, lamda):
    """
    Funcion de distribucion acumulada de una exponencial.
    """
    return 1 - math.exp(-lamda*x)


def pValor(r, n, d):
    """
    r = Numero de simulaciones
    n = muestra
    d = Estadistico
    """
    uniformes = []
    valoresD = []
    exitos = 0 # Cantidad de veces que se cumple que D >= d

    for _ in xrange(r):
        # Generamos n U ~ U(0, 1)
        for _ in xrange(n):
            uniformes.append(random.random())
        uniformes.sort()

        # Calculamos D
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
    """
    valores = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
    #valores = [66, 72, 81, 94, 112, 116, 124, 140, 145, 155]
    valores.sort()

    n = len(valores) # Tamaño de la muestra
    
    # Calculamos D
    valoresD = [] # Contendra los elementos del conjunto D+ y D-
    j = 1
    for valor in valores:
        F = acumuladaExponencial(valor, 1/50.0)
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    D = max(valoresD)

    p_valor = pValor(10000, n, D)

    # if p_valor < alfa:
    #     print "Se rechaza H0"
    # elif p_valor > alfa:
    #     print "No se rechaza H0"

    return p_valor


def chiCuadrado():
    valores = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
    n = len(valores) # Tamaño de la muestra
    k = 6



print "p-valor =", testKS()
