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
        # Generamos n U ~ U(0, 1) y las ordenamos
        uniformes = [random.random() for _ in xrange(n)]
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
    Estima la media de una lista de valores.
    """
    return sum(lista)/float(len(lista))


def estimacionDE(lista):
    """
    Estima la Desviacion Estandar de una lista de valores.
    """
    media = estimacionMedia(lista)

    suma = 0
    for valor in lista:
        suma += (valor - media)**2

    return math.sqrt(suma/float(len(lista)))


def testKS():
    """
    Test de Kolmogorov-Smirnov.
    """
    valores = [91.9, 97.8, 111.4, 122.3, 105.4, 95, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
    valores.sort()

    # Estimacion de la media y desviacion estandar
    media = estimacionMedia(valores)
    des_est = estimacionDE(valores)

    n = len(valores) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contiene los elementos del conjunto D+ y D-
    j = 1
    for valor in valores:
        F = fi((valor - media)/des_est)
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
