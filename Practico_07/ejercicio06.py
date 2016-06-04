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


def testKS():
    """
    Test de Kolmogorov-Smirnov.
    """
    # Generamos 10 exponenciales de lambda 1 y las ordenamos
    valores = [exponencial(1) for _ in xrange(10)]
    valores.sort()
    
    n = len(valores) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contendra los elementos del conjunto D+ y D-
    j = 1
    for valor in valores:
        F = acumuladaExponencial(valor, 1)
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    d = max(valoresD) # Valor observado

    p_valor = pValor(10000, n, d)

    # if p_valor < alfa: # o <= (menor igual)
    #     # Se rechaza la H0 a un nivel alfa
    #     print "Se rechaza H0"
    # elif p_valor > alfa:
    #     # No hay evidencia suficiente para rechazar H0 a un nivel alfa
    #     print "No se rechaza H0"

    return p_valor


def esperanza(n):
    """
    Calcula la esperanza del p-valor con el Test de KS.
    """
    a = 0
    for _ in xrange(n):
        a += testKS()

    return a/float(n)


# Nivel de confianza = 1 - alfa
# Alfas comunes: 0.05, 0.01, 0.1
# print "p-valor =", testKS()
print "p-valor =", esperanza(100)
