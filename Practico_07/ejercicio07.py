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


def estimacionMedia(lista):
    """
    Estimacion de la media en base a una lista de valores.
    Clase: Analisis estadistico de datos simulados. Estimadores puntuales
    Filmina: 12
    """
    return sum(lista)/float(len(lista))


def testKS(alfa):
    """
    Test de Kolmogorov-Smirnov.
    """
    valores = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
    valores.sort()

    # Estimamos la media muestral
    media_muestral = estimacionMedia(valores)

    # Estimacion de lambda
    lamda = 1/float(media_muestral)

    n = len(valores) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contiene los elementos del conjunto D+ y D-
    j = 1
    for valor in valores:
        F = acumuladaExponencial(valor, lamda)
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    d = max(valoresD) # Valor observado

    p_valor = pValor(10000, n, d)

    if p_valor < alfa:
        print("Se rechaza H0")
    elif p_valor > alfa:
        print("No se rechaza H0")

    return p_valor


# Nivel de confianza = 1 - alfa
# Alfas comunes: 0.05, 0.01, 0.1
print("p-valor =", testKS(0.05))
