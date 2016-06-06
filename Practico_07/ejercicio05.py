# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *

# T = sumatoria(1, k, (fo - fe)^2/fe)
# fo = Ni
# fe = n*pi

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


def probabilidadBinomial(n, p, i):
    """
    Funcion de masa de una distribucion Binomial B(n, p)
    """
    combinatorio = math.factorial(n)/float(math.factorial(i) * math.factorial(n-i))

    return combinatorio * (p**i) * ((1 - p)**(n-i))


def chiCuadrado():
    """
    Calculo del p-valor de un conjunto de datos segun la distribucion Binomial.
    """
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()
    n = len(datos) # Tamaño de la muetra
    k = 3 # Cantidad de intervalos
    N = [3, 6, 9] # Frecuencias observadas

    # Estimamos la probabilidad 'p' = 0.618
    p = estimacionP(8, datos)

    m = 1 # Cantidad de parametros estimados

    # Calculamos las 9 (0...8) probilidades de una B(8, p)
    pro_binomial = [probabilidadBinomial(8, p, i) for i in xrange(9)]

    # Obtenemos las probabilidades de los intervalos
    p1 = pro_binomial[0] + pro_binomial[1] + pro_binomial[2]
    p2 = pro_binomial[3] + pro_binomial[4] + pro_binomial[5]
    p3 = pro_binomial[6] + pro_binomial[7] + pro_binomial[8]
    prob = [p1, p2, p3]

    t = estadisticoT(k, n, N, prob) # Valor observado

    grados_libertad = k - m - 1 # En este caso son 1

    p_valor = pValor(grados_libertad, t)

    return p_valor


def simulacion(r):
    """
    Algoritmo, para calcular el p-valor, que esta en el Libro de Simulacion.
    """
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    datos.sort()
    n = len(datos) # Tamaño de la muetra
    k = 3 # Cantidad de intervalos
    N = [3, 6, 9] # Frecuencias observadas

    # Estimamos la probabilidad 'p' = 0.618
    p = estimacionP(8, datos)

    m = 1 # Cantidad de parametros estimados

    # Calculamos las 9 (0...8) probilidades de una B(8, p)
    pro_binomial = [probabilidadBinomial(8, p, i) for i in xrange(9)]

    # Obtenemos las probabilidades de los intervalos
    p1 = pro_binomial[0] + pro_binomial[1] + pro_binomial[2]
    p2 = pro_binomial[3] + pro_binomial[4] + pro_binomial[5]
    p3 = pro_binomial[6] + pro_binomial[7] + pro_binomial[8]
    prob = [p1, p2, p3]

    t = estadisticoT(k, n, N, prob) # Valor observado

    exitos = 0 # Cantidad de veces que Ti >= t

    for _ in xrange(r):
        Y = [binomial(8, p) for _ in xrange(n)]

        N0 = 0
        N1 = 0
        N2 = 0
        for i in xrange(n):
            if 0 <= Y[i] <= 2:
                N0 += 1
            elif 3 <= Y[i] <= 5:
                N1 += 1
            elif 6 <= Y[i] <= 8:
                N2 += 1
        N_sim= [N0, N1, N2]
        # N0 = sum( [Y.count(i) for i in [0, 1, 2]] )
        # N1 = sum( [Y.count(i) for i in [3, 4, 5]] )
        # N2 = sum( [Y.count(i) for i in [6, 7, 8]] )
        # N_sim = [N0, N1, N2]

        p_sim = estimacionP(8, Y)

        pro_binomial = [probabilidadBinomial(8, p_sim, i) for i in xrange(9)]
        p1 = pro_binomial[0] + pro_binomial[1] + pro_binomial[2]
        p2 = pro_binomial[3] + pro_binomial[4] + pro_binomial[5]
        p3 = pro_binomial[6] + pro_binomial[7] + pro_binomial[8]
        prob_sim = [p1, p2, p3]

        T = estadisticoT(k, n, N_sim, prob_sim)

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor



print "Chi-Cuadrado --> p-valor =", chiCuadrado()
print "Simulacion --> p-valor =", simulacion(10000)
