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
    p_blanca = 1/4.0
    p_rosa = 1/2.0
    p_roja = 1/4.0

    guisantes = 564

    blancas = 141
    rosas = 291
    rojas = 132

    N = [blancas, rosas, rojas]
    p = [p_blanca, p_rosa, p_roja]

    T = estadistico(3, guisantes, N, p)

    grados_libertad = 2

    p_valor = pValor(grados_libertad, T)

    return p_valor


def simulacion01(r):
    """
    Algoritmo que esta en el libro de Simulacion.
    """
    n = 564 # Tamaño de la muestra
    k = 3 # Cantidad de intevalos
    prob = [0.25, 0.50, 0.25] # Probabilidades
    N = [141, 291, 132]
    t = estadistico(3, n, N, prob) # Estadistico

    prob_acumuladas = [0.25, 0.75, 1.0]
    exitos = 0 # Cantidad de veces que Ti >= t

    fe = [] # Frecuencias Observadas
    
    # Obtenemos las Frecuencias Esperadas
    for i in xrange(len(prob)):
        fe.append(n*prob[i])

    # Hacemos r simulaciones
    for _ in xrange(r):

        fo = [] # Frecuencias Observadas (son los N)
        for _ in xrange(k):
            fo.append(0)
        
        # Calculamos las Frecuencias Obsevadas en un experimento
        for _ in xrange(n):
            u = random.random()
            i = 0
            while u >= prob_acumuladas[i]:
                i += 1

            fo[i] += 1

        T = 0
        # Sumamos todos los estadisticos Ti
        for i in xrange(k):
            Ti = (fo[i] - fe[i])**2/float(fe[i]) # Calculamos los estadistios Ti
            T +=  Ti

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor


def simulacion02(r):
    """
    Algoritmo que esta en las Filminas.
    """
    n = 564 # Tamaño de la muestra
    k = 3 # Cantidad de intevalos
    prob = [0.25, 0.50, 0.25] # Probabilidades
    N = [141, 291, 132] # Ni
    t = estadistico(k, n, N, prob) # Estadistico
    exitos = 0 # Cantidad de veces que Ti >= t

    for _ in xrange(r):
        Y = []
        N = []
        # Generamos los Y's
        for _ in xrange(n):
            u = random.random()
            if u < 0.5:
                Y.append(2)
            elif u < 0.75:
                Y.append(1)
            elif u >= 0.75:
                Y.append(3)

        # Generamos los Nj
        # j va de 1 a k
        for j in xrange(1, k+1):
            N.append(Y.count(j))

        # Calculamos el estadistico correspondiente
        T = estadistico(k, n, N, prob)

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor



print "Chi-Cuadrado --> p-valor =", chiCuadrado()
print "Simulacion 1 --> p-valor =", simulacion01(10000)
print "Simulacion 2 --> p-valor =", simulacion02(10000)