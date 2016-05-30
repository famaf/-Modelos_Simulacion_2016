# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


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


# binomial(n, p)

def estimacion():
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()

    p = estimacionP(8, datos) # Estimamos la probabilidad 'p'

    n = len(datos) # Tamaño de la muetra

    media = 8 * p
    des_est = math.sqrt(8 * p * (1-p))

    # Calculamos D
    valoresD = [] # Contiene los elementos del conjunto D+ y D-
    j = 1
    for valor in datos:
        z = (valor - media)/des_est
        F = fi(z)
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



print "p-valor =", estimacion()
