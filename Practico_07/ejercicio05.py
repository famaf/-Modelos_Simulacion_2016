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


def chiCuadrado():
    """
    Calculo del p-valor de un conjunto de datos segun la distribucion Binomial.
    """
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()

    # Estimamos la probabilidad 'p' = 0.618
    p = estimacionP(8, datos)

    m = 1 # Cantidad de parametros estimados
    n = len(datos) # Tamaño de la muetra
    k = 3 # Cantidad de intervalos

    N = [3, 6, 9] # Frecuencias observadas

    # Calculamos las 9 probilidades de una B(8, p)
    pro_binomial = []
    for i in xrange(9):
        pro_binomial.append(calculoBinomial(8, p, i))

    # Obtenemos las probabilidades de los intervalos
    p1 = pro_binomial[0] + pro_binomial[1] + pro_binomial[2]
    p2 = pro_binomial[3] + pro_binomial[4] + pro_binomial[5]
    p3 = pro_binomial[6] + pro_binomial[7] + pro_binomial[8]
    prob = [p1, p2, p3]

    t = estadisticoT(k, n, N, prob) # Valor observado

    grados_libertad = k - m - 1 # En este caso son 7

    p_valor = pValor(grados_libertad, t)

    return p_valor


def simulacion01(r):
    """
    Algoritmo, para calcular el p-valor, que esta en el Libro de Simulacion.
    """
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()

    # Estimamos la probabilidad 'p' = 0.618
    p = estimacionP(8, datos)

    m = 1 # Cantidad de parametros estimados
    n = len(datos) # Tamaño de la muetra
    k = 3 # Cantidad de intervalos

    N = [3, 6, 9] # Frecuencias observadas

    # Calculamos las 9 probilidades de una B(8, p)
    pro_binomial = []
    for i in xrange(9):
        pro_binomial.append(calculoBinomial(8, p, i))

    # Obtenemos las probabilidades de los intervalos
    p1 = pro_binomial[0] + pro_binomial[1] + pro_binomial[2]
    p2 = pro_binomial[3] + pro_binomial[4] + pro_binomial[5]
    p3 = pro_binomial[6] + pro_binomial[7] + pro_binomial[8]
    prob = [p1, p2, p3]

    t = estadisticoT(k, n, N, prob) # Valor observado

    prob_acumuladas = [p1, p1+p2, p1+p2+p3]

    exitos = 0 # Cantidad de veces que Ti >= t

    fe = [] # Frecuencias Observadas
    
    # Obtenemos las Frecuencias Esperadas
    for i in xrange(len(prob)):
        fe.append(n*prob[i])

    # Hacemos r simulaciones
    for _ in xrange(r):
        # Frecuencias Observadas (son los N)
        fo = [0 for _ in xrange(k)]

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



print "p-valor =", chiCuadrado()
print "p-valor =", simulacion01(10000)
