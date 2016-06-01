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


def chiCuadrado():
    """
    Calcula el p-valor por medio de una aproximacion Chi-Cuadrada.
    """
    lanzamientos = 1000

    valor1 = 158
    valor2 = 172
    valor3 = 164
    valor4 = 181
    valor5 = 160
    valor6 = 165

    N = [valor1, valor2, valor3, valor4, valor5, valor6]
    p = [1/6.0 for _ in xrange(6)]

    t = estadisticoT(6, lanzamientos, N, p) # Valor observado

    grados_libertad = 5

    p_valor = pValor(grados_libertad, t)

    return p_valor


def simulacion01(r):
    """
    Algoritmo, para calcular el p-valor, que esta en el Libro de Simulacion.
    """
    n = 1000 # Tamaño de la muestra
    k = 6 # Cantidad de intevalos
    prob = [1/6.0 for _ in xrange(6)] # Probabilidades
    N = [158, 172, 164, 181, 160, 165]
    t = estadisticoT(k, n, N, prob) # Valor observado

    prob_acumuladas = [1/6.0, 1/3.0, 0.5, 2/3.0, 5/6.0, 1.0]
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
    Algoritmo, para calcular el p-valor, que esta en las Filminas.
    """
    n = 1000 # Tamaño de la muestra
    k = 6 # Cantidad de intevalos
    prob = [1/6.0 for _ in xrange(6)] # Probabilidades
    N = [158, 172, 164, 181, 160, 165]
    t = estadisticoT(k, n, N, prob) # Valor observado
    exitos = 0 # Cantidad de veces que Ti >= t

    for _ in xrange(r):
        Y = []
        N = []
        # Generamos los Y's
        for _ in xrange(n):
            Y.append(random.randint(1, 6))
        
        # Generamos los Nj
        # j va de 1 a k
        for j in xrange(1, k+1):
            N.append(Y.count(j))

        # Calculamos el estadistico T correspondiente
        T = estadisticoT(k, n, N, prob)

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor



print "Chi-Cuadrado --> p-valor =", chiCuadrado()
print "Simulacion 1 --> p-valor =", simulacion01(10000)
print "Simulacion 2 --> p-valor =", simulacion02(10000)
